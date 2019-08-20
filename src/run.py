# !/usr/bin/env python
import os
import sys
from functools import partial

from rasa.cli.utils import get_validated_path
from rasa.constants import DEFAULT_ENDPOINTS_PATH, DEFAULT_MODELS_PATH, DEFAULT_RASA_PORT
from rasa.core.run import load_agent_on_start
from rasa.core.utils import AvailableEndpoints
from rasa.model import get_model
from sanic import Sanic
from sanic_cors import CORS

from src.views import server

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.views import api_bp, html_bp, json_bp

# app = Sanic(__name__)

# app.blueprint(api_bp)
# app.blueprint(html_bp)
# app.blueprint(json_bp)

# TODO 从配置文件获取配置
BASE_CORE_PATH = "core/"
enable_api = True
cors = None
auth_token = None
jwt_secret =None
jwt_method =None
# aws,gcs,azure
remote_storage = None
endpoints = get_validated_path(
        BASE_CORE_PATH+"endpoints.yml", "endpoints", DEFAULT_ENDPOINTS_PATH, True
    )
_endpoints = AvailableEndpoints.read_endpoints(endpoints)
port = DEFAULT_RASA_PORT

# model = get_validated_path(BASE_CORE_PATH+"models/", "model", DEFAULT_MODELS_PATH)
model_path = BASE_CORE_PATH+"models/"

if __name__ == "__main__":

    if not model_path:
        print(
            "No model found. Train a model before running the server"
        )

    if enable_api:
        app = server.create_app(
            cors_origins=cors,
            auth_token=auth_token,
            jwt_secret=jwt_secret,
            jwt_method=jwt_method,
            endpoints=endpoints,
        )
    else:
        app = Sanic(__name__, configure_logging=False)
        CORS(app, resources={r"/*": {"origins": cors or ""}}, automatic_options=True)

    app.register_listener(
        partial(load_agent_on_start, model_path, _endpoints, remote_storage),
        "before_server_start",
    )
    app.blueprint(api_bp)
    app.blueprint(html_bp)
    app.blueprint(json_bp)
    app.run(host="0.0.0.0", port=port)
