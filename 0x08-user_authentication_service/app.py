#!/usr/bin/env python3
""" Route module for the API """
from db import DB
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ Route for authentication service API """
    return jsonify({"message": "Bienvenue"})
