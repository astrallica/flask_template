# -*- coding:utf-8 -*-

from flask_restful import Resource, marshal_with, reqparse
from common.mods import db
from common.models import Test
from common.fields import test_fields
from common.api_errors import Invalid, NotFound

__author__ = "Philgyu, Seong"
__email__ = "phil.seong@funlab.kr"

KEY_NAME = "name"


class HelloApi(Resource):
    def get(self):
        return "hi!!!"
