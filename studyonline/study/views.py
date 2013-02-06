#-*- coding:utf-8 -*-
import os
from google.appengine.ext import db
from google.appengine.ext.webapp import template
import webapp2
import common
import main
from study.models import UserInfo

__author__ = 'Prince'
"""
处理根目录静态页面
以及首页
"""
class HtmlHandler(webapp2.RequestHandler):
    def get(self,htmlurl = "",ext = ""):
        if (len(htmlurl) and ext =='.html'):
            path = os.path.join(os.path.dirname(main.__file__)+"/templates",htmlurl+ext)
            self.response.out.write(template.render(path,{}))
        else:
            path = os.path.join(os.path.dirname(main.__file__)+"/templates","index.html")
            self.response.out.write(template.render(path,{}))
class LoginHandler(common.BaseSessionHandler):
    def post(self) :
        username = self.request.get("username")
        password = self.request.get("password")
        query = db.GqlQuery("SELECT * FROM UserInfo WHERE username =:1 AND password =:2",username,password)
        res = query.fetch(10)
        len(res)

        self.session['user'] = res[0].username
        path = os.path.join(os.path.dirname(main.__file__)+"/templates","index.html")
        self.response.out.write(template.render(path,{}))
class RegistHandler(common.BaseSessionHandler):
    def post(self):
        user = UserInfo ()
        user.email = self.request.get("email")
        user.username = self.request.get("userName")
        user.password = self.request.get("password")
        user.save()
        self.session['user'] = user
        path = os.path.join(os.path.dirname(main.__file__)+"/templates","index.html")
        self.response.out.write(template.render(path,{}))