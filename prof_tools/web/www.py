# coding=utf8

from flask import Flask
from flask_cors import *
from sar_service import route_entity

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(route_entity, url_prefix="/prof")


def load_app():
    info_ext_service.init_predictor(cfg)
    return app


if __name__ == "__main__":
    load_app()
    app.run('0.0.0.0', port=8890)
