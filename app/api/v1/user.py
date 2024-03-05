# -*- coding: utf-8 -*-
from flask import Blueprint

# @Time : 2024/3/5 15:04

# @Author : javin9
# @Email : 1330361087@qq.com
# @File : user.py

user = Blueprint('user', __name__)


@user.route("/list")
def get_user():
  return ["用户内容"]
