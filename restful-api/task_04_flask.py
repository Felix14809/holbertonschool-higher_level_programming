#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "<p>Welcome to the FLask API!<p>"


@app.route("/data")
def data():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
         "bart": {"name": "bart"},
         "bert": {"name": "bert"},
         "bort": {"name": "bort"}
         }
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user_info(username):
    try:
        user = users.get(username)
    except ValueError:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error":"Invalid JSON"}), 400
    username = data.get("username")
    if not username:
        return jsonify({"error":"Username is required"}), 400
    if username in users:
        return jsonify({"error":"Username already exists"}), 409
    users[username] = data
    return jsonify({"message":"User added", "user": data}), 201


if __name__ == "__main__":
    app.run()