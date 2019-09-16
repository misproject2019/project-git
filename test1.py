# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:29:18 2019

@author: Julia
"""
import pandas as pd
import numpy as np
import tensorflow as tf

ratings_df = pd.read_csv('user_rating.csv')
movies_df = pd.read_csv('rest.csv')
movies_df['MovieRow'] = movies_df.index

ratings_df = pd.merge(ratings_df, movies_df, on = 'movieID')

ratings_df = ratings_df[['userID','MovieRow','rating']]

userNo = ratings_df['userID'].max()+1
movieNo = ratings_df['MovieRow'].max()+1

rating = np.zeros((movieNo,userNo))
flag = 0
#获取合并表中的列数
ratings_df_length = np.shape(ratings_df)[0]
#遍历矩阵，将评分填入表中
for index,row in ratings_df.iterrows():
    rating[int(row['MovieRow']), int(row['userID'])] = row['rating']
    flag += 1
record = rating > 0
record = np.array(record, dtype = int)

def normalizeRatings(rating, record):
    #获取电影的数量m和用户的数量n
    m,n = rating.shape
    #rating_mean-电影平均分   rating_norm-标准化后的电影得分
    rating_mean = np.zeros((m,1))
    rating_norm = np.zeros((m,n))
    for i in range(m):
        idx = record[i,:]!=0
        rating_mean[i] = np.mean(rating[i,idx])
        rating_norm[i,idx] -= rating_mean[i]
    return rating_norm, rating_mean
rating_norm, rating_mean = normalizeRatings(rating, record)
rating_norm = np.nan_to_num(rating_norm)
rating_mean = np.nan_to_num(rating_mean)

num_features = 10
X_parameters = tf.Variable(tf.random.normal([movieNo, num_features],stddev = 0.35))
Theta_parameters = tf.Variable(tf.random.normal([userNo, num_features],stddev = 0.35))
loss = 1/2 * tf.reduce_sum(((tf.matmul(X_parameters, Theta_parameters, transpose_b=True) - rating_norm) * record) ** 2) + 1/2 * (tf.reduce_sum(X_parameters ** 2) + tf.reduce_sum(Theta_parameters ** 2)) 
optimizer = tf.compat.v1.train.AdamOptimizer(1e-4)
train = optimizer.minimize(loss)
#訓練模型
tf.compat.v1.summary.scalar('loss', loss)
summaryMerged = tf.compat.v1.summary.merge_all()
#merge_all 可以将所有summary全部保存到磁盘，以便tensorboard显示。
filename = './movie_tensorborad'
writer = tf.compat.v1.summary.FileWriter(filename)
#指定一个文件用来保存图。
sess = tf.compat.v1.Session()
#定义一个session
init = tf.compat.v1.global_variables_initializer()
sess.run(init)
for i in range(5000):
    _, movie_summary = sess.run([train, summaryMerged])
    writer.add_summary(movie_summary, i)

Current_X_parameters, Current_Theta_parameters = sess.run([X_parameters, Theta_parameters])
# Current_X_parameters为用户内容矩阵，Current_Theta_parameters用户喜好矩阵
predicts = np.dot(Current_X_parameters,Current_Theta_parameters.T) + rating_mean
errors = np.sqrt(np.sum((predicts - rating)**2))
print(errors)

userId = input('您要向哪位用户进行推荐呢？请输入用户编号：')
sortedResult = predicts[:, int(userId)].argsort()[::-1]
idx = 0
print('为该用户推荐的评分最高的20部电影是：')
for i in sortedResult:
    print('score: %.3f, movie name: %s' % (predicts[i, int(userId)], movies_df.iloc[i]['movieID']))
    idx += 1
    if idx == 20:
        break