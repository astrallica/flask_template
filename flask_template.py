from flask import Flask
from common.mods import api, db
from common.api_errors import errors
from resources.test_api import TestApi
from resources.hello_api import HelloApi

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def register_apis():
    api.add_resource(TestApi, "/test/<int:topic_id>", "/test")
    api.add_resource(HelloApi, "/hello")


app.config.from_pyfile("configs.py")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

register_apis()

db.init_app(app)
api.init_app(app)
api.errors = errors

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000
    )
