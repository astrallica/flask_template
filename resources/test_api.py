# -*- coding:utf-8 -*-

from flask_restful import Resource, marshal_with, reqparse
from common.mods import db
from common.models import Test
from common.fields import test_fields
from common.api_errors import Invalid, NotFound

__author__ = "Philgyu, Seong"
__email__ = "phil.seong@funlab.kr"

KEY_NAME = "name"


class TestApi(Resource):
    @marshal_with(test_fields)
    def get(self):
        users = Test.query.all()
        return users

    def post(self):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument(KEY_NAME, type=str, required=True)

        args = post_parser.parse_args()
        name = args[KEY_NAME]

        test_user = Test.query.filter(Test.name == name).first()

        if test_user is not None:
            raise Invalid

        test_user = Test(name=name)

        db.session.add(test_user)
        db.session.commit()

        return {"return": "ok"}

    @marshal_with(test_fields)
    def edit(self, user_id):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument(KEY_NAME, type=str, required=True)

        args = post_parser.parse_args()
        name = args[KEY_NAME]

        test_user = Test.query.filter(Test.id == user_id).first()

        if test_user is None:
            raise NotFound

        test_user.name = name

        db.session.merge(test_user)
        db.session.commit()

        return test_user

    def delete(self, user_id):
        delete_user = Test.query.filter(Test.id == user_id).first()

        if delete_user is None:
            raise NotFound

        db.session.delete(delete_user)
        db.session.commit()

        return {"return": "deleted"}
