# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:52:22 2019

@author: Julia
"""
import tensorflow.compat.v1 as tf
import pandas as pd
import numpy as np
import FirstWindow
#第一步：------------------------收集和清洗資料
df = pd.read_csv('早餐早午餐中式.txt', sep='\t', names=['user_na','rest_id','score'])
df['user_id'] = df.index

df['movieRow'] = df.index
movies_df = df[['movieRow', 'rest_id']]
movies_df.to_csv('rest1.csv', index=False, header=True, encoding='utf-8')

ratings_df = pd.merge(df, movies_df, on='rest_id')
print(ratings_df)
ratings_df = ratings_df[['user_id', 'movieRow_x', 'score']]
ratings_df.to_csv('score1.csv', index=False, header=True, encoding='utf-8')
#第二步：-----------------------建立評分矩陣rating和評分紀錄矩陣record
userNo=ratings_df['user_id'].count()
movieNo=ratings_df['movieRow_x'].count()
#userNo = tf.cast(userNo,dtype=tf.int32)
#movieNo = tf.cast(movieNo,dtype=tf.int32)
rating = np.zeros((movieNo, userNo))
flag = 0
ratings_df_length = np.shape(ratings_df)[0]
for index, row in ratings_df.iterrows():
    rating[int(row['movieRow_x'])][int(row['user_id'])] = row['score']
    flag += 1
record = rating > 0
record = np.array(record, dtype=int)
#第三步：----------------------------構建模型
def normalizeRatings(rating, record):
    m, n = rating.shape
    rating_mean = np.zeros((m, 1))
    rating_norm = np.zeros((m, n))
    for i in range(m):
        idx = (record[i, :] != 0)
        rating_mean[i] = np.mean(rating[i, idx])
        rating_norm[i, idx] = rating[i, idx] - rating_mean[i]
    return rating_norm, rating_mean

rating_norm, rating_mean = normalizeRatings(rating, record)
rating_norm = np.nan_to_num(rating_norm)
rating_mean = np.nan_to_num(rating_mean)
# 構建模型
num_features = 12
X_parameters = tf.Variable(tf.random_normal([movieNo, num_features], stddev = 0.35))
Theta_parameters = tf.Variable(tf.random_normal([userNo, num_features], stddev = 0.35))
loss = 1/2 * tf.reduce_sum(((tf.matmul(X_parameters, Theta_parameters, transpose_b=True) - rating_norm) * record) ** 2) + 0.5*(1/2 * (tf.reduce_sum(X_parameters ** 2) + tf.reduce_sum(Theta_parameters ** 2)))
# 基於內容的推薦演算法模型
train = tf.train.AdamOptimizer(1e-3).minimize(loss)
# 第四步：------------------------------------訓練模型
tf.summary.scalar('train_loss', loss)
summaryMerged = tf.summary.merge_all()
filename = 'movie_tensorborad.csv'
writer = tf.summary.FileWriter(filename)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
for i in range(2000):
    _, movie_summary = sess.run([train, summaryMerged])
    writer.add_summary(movie_summary, i)
# 第五步：-------------------------------------評估模型
Current_X_parameters, Current_Theta_parameters = sess.run([X_parameters, Theta_parameters])
predicts = np.dot(Current_X_parameters, Current_Theta_parameters.T) + rating_mean
errors = np.sqrt(np.sum(((predicts - rating) * record)**2))
# 第六步：--------------------------------------構建完整的推薦系統
FirstWindow.na="1"
user_na = FirstWindow.na
user_id=df[df['user_na'].isin(['A'])].index.values[0]
print(user_id)
sortedResult = predicts[:, int(user_id)].argsort()[::-1]
idx = 0
for i in sortedResult:
    a=movies_df.iloc[i]['rest_id']
    print(a)
    #print(u'評分: %.1f, 店名: %s' % (predicts[i, int(user_id)]-2, movies_df.iloc[i]['rest_id']))
    idx += 1
    if idx == 1:
        break
    
    
'''FirstWindow.nam="1"
user_id = FirstWindow.nam
sortedResult = predicts[:, int(user_id)].argsort()[::-1]
idx = 0
global a
for i in sortedResult:
    global a
    a=df.iloc[i]['user_na']
    idx += 1
    if idx == 1:
        break'''