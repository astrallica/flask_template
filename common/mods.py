# -*- coding:utf-8 -*-
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

__author__ = "Philgyu, Seong"
__email__ = "phil.seong@funlab.kr"

db = SQLAlchemy()

bcrypt = Bcrypt()

api = Api()

login_manager = LoginManager()