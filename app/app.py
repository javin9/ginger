# -*- coding: utf-8 -*-
from flask import Flask


# @Time : 2024/3/5 14:11

# @Author : javin9
# @Email : 1330361087@qq.com
# @File : app.py

def register_blueprints(app):
  from app.api.v1 import book, user
  app.register_blueprint(user, url_prefix='/v1/user')
  app.register_blueprint(book, url_prefix='/v1/book')


def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config.setting')
  app.config.from_object('app.config.secure')
  register_blueprints(app)
  return app
