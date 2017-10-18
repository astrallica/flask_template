# -*- coding:utf-8 -*-
from flask_restful import fields

__author__ = "Philgyu, Seong"
__email__ = "phil.seong@funlab.kr"


session_type_fields = {
    "type": fields.String
}

session_fields = {
    "id": fields.Integer,
    "access_token": fields.String,
    "types": fields.Nested(session_type_fields)
}

test_fields = {
    "id": fields.Integer,
    "name": fields.String
}
