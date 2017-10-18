# -*- coding:utf-8 -*-
from werkzeug.exceptions import HTTPException

__author__ = "Philgyu, Seong"
__email__ = "phil.seong@funlab.kr"


class Forbidden(HTTPException):
    pass


class InternalServerError(HTTPException):
    pass


class Invalid(HTTPException):
    pass


class NotFound(HTTPException):
    pass


class SQLAlchemyError(HTTPException):
    pass


# message 는 소문자로 시작, 마침표를 찍지 않는다.
errors = {
    "Forbidden": {
        "message": "forbidden",
        "status": 403
    },
    "NotFound": {
        "message": "not found",
        "status": 404
    },
    "SQLAlchemyError": {
        "message": "sql error",
        "status": 500
    },
    "Invalid": {
        "message": "invalid",
        "status": 400
    },
    "InternalServerError": {
        "message": "something wrong with api server",
        "status": 500
    }
}