#-*- coding:utf-8 -*-
from google.appengine.ext import db

__author__ = 'Prince'

class UserInfo(db.Model):
    id = db.Key()
    username = db.StringProperty()
    password = db.StringProperty()
    email = db.EmailProperty()
    neckName = db.StringProperty()
    thirdinfo = db.StringProperty(multiline=True)
    age =db.IntegerProperty()
    gender = db.StringProperty(choices=set(['男','女']))
    registDate = db.DateTimeProperty(auto_now=True)
    lastLoginTs = db.DateTimeProperty()
    cookies = db.StringProperty()
