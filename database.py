# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:06:35 2019

@author: Julia
"""
class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.user = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.user = {}

        for line in self.file:
            userid, restid, score = line.strip().split("	")
            self.user[userid] = (restid,score)

        self.file.close()

    def add_user(self, userid, restid,score):
        self.user[userid.strip()] = (str(restid).strip(),str(score).strip())
        self.save()

    def save(self):
        with open(self.filename, "w") as f:
            for users in self.user:
                f.write(users + "	" + self.user[users][0] + "	" + self.user[users][1] + "\n")