# -*- coding: utf-8 -*-
from flask import Blueprint

# @Time : 2024/3/5 15:05

# @Author : javin9
# @Email : 1330361087@qq.com
# @File : book.py

book = Blueprint('book', __name__)


@book.route("/list")
def get_book():
  return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
