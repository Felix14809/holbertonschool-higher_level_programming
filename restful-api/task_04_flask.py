#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}