# -*- coding:utf-8 -*-
# from flask_login import current_user
# from sqlalchemy.ext.hybrid import hybrid_property
# from sqlalchemy.orm.util import aliased
# from sqlalchemy.sql.functions import func
#
# from common.api_errors import NotFound
from common.mods import db

__author__ = "Philgyu, Seong"
__email__ = "phil.seong@funlab.kr"


class SessionType(object):
    EMAIL = "email"

    def __init__(self, type):
        self.type = type


# class Session(object):
#     def __init__(self, user_id, generated_access_token, username):
#         session_user = User.query.filter(User.id == user_id).first()
#
#         if session_user is None:
#             raise UserNotFound
#
#         self.id = session_user.id
#         self.access_token = generated_access_token
#         self.username = username
#
#         self.types = []
#
#         if session_user.password is not None:
#             self.types.append(SessionType(SessionType.EMAIL))
#         elif session_user.fb_id is not None:
#             self.types.append(SessionType(SessionType.FB))
#         elif session_user.twitter_id is not None:
#             self.types.append(SessionType(SessionType.TWITTER))
#
#
# class User(db.Model):
#     # 소셜 계정 미적용
#     id = db.Column(db.INT, primary_key=True)
#     access_token = db.Column(db.VARCHAR(64))
#     fb_access_token = db.Column(db.VARCHAR(256))
#     username = db.Column(db.VARCHAR(32), unique=True)
#     email = db.Column(db.VARCHAR(64), unique=True)
#     password = db.Column(db.VARCHAR(64))
#     name = db.Column(db.VARCHAR(32))
#     zipcode = db.Column(db.INT)
#     address1 = db.Column(db.VARCHAR(128))
#     address2 = db.Column(db.VARCHAR(128))
#     recent_name = db.Column(db.VARCHAR(32))
#     recent_zipcode = db.Column(db.INT)
#     recent_add1 = db.Column(db.VARCHAR(128))
#     recent_add2 = db.Column(db.VARCHAR(128))
#     recent_phone = db.Column(db.VARCHAR(16))
#     phone = db.Column(db.VARCHAR(16))
#     level = db.Column(db.INT)
#     point = db.Column(db.INT)
#     region = db.Column(db.VARCHAR(32))
#     seller_level = db.Column(db.INT)
#     bank_account = db.Column(db.VARCHAR(32))
#     biz_num = db.Column(db.VARCHAR(32))
#     biz_name= db.Column(db.VARCHAR(32))
#     recommender_id = db.Column(db.INT)
#     profile_thumb_url = db.Column(db.VARCHAR(128))
#     last_logged_at = db.Column(db.DATETIME)
#     introduce = db.Column(db.VARCHAR(64))
#     created_at = db.Column(db.DATETIME)
#     is_activated = db.Column(db.INT)
#
#     post = db.relationship("Post", backref="user", cascade="all,delete", lazy="dynamic")
#     like = db.relationship("Like", backref="user", cascade="all,delete", lazy="dynamic")
#     reply = db.relationship("Reply", backref="user", cascade="all,delete", lazy="dynamic")
#     basket = db.relationship("Basket", backref="user", cascade="all,delete", lazy="dynamic")
#
#     def __init__(self, username, created_at, last_logged_at, profile_thumb_url, access_token="", level=0, point=0,
#                  seller_level=0, is_activated=0,
#                  password=None, name=None, zipcode=None, address1=None, address2=None,
#                  recent_name=None, recent_zipcode=None, recent_add1=None, recent_add2=None, recent_phone=None,
#                  phone=None, region=None, bank_account=None, biz_num=None, biz_name=None, recommender_id=None,
#                  introduce=None, email=None):
#         self.access_token = access_token
#         self.username = username
#         self.email = email
#         self.password = password
#         self.name = name
#         self.zipcode = zipcode
#         self.address1 = address1
#         self.address2 = address2
#         self.recent_name = name
#         self.recent_zipcode = recent_zipcode
#         self.recent_add1 = recent_add1
#         self.recent_add2 = recent_add2
#         self.recent_name = recent_name
#         self.recent_phone = recent_phone
#         self.phone = phone
#         self.level = level
#         self.point = point
#         self.region = region
#         self.seller_level = seller_level
#         self.bank_account = bank_account
#         self.biz_num = biz_num
#         self.biz_name = biz_name
#         self.recommender_id = recommender_id
#         self.profile_thumb_url = profile_thumb_url
#         self.last_logged_at = last_logged_at
#         self.introduce = introduce
#         self.created_at = created_at
#         self.is_activated = is_activated
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anoymous(self):
#         return False
#
#     def get_id(self):
#         return self.id
#
#     @hybrid_property
#     def is_me(self):
#         if not current_user.is_authenticated:
#             return False
#         return current_user.id == self.id


class Test(db.Model):
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.VARCHAR(45))

    def __init__(self, name):
        self.name = name
