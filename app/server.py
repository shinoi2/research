#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gevent.monkey
gevent.monkey.patch_all(thread=False)
from flask import Flask
from flask_cors import CORS
from api import api_bp

app = Flask(__name__)

CORS(app)
app.config["JSON_AS_ASCII"] = False
app.register_blueprint(api_bp)
