#!/user/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

# Entry point for running with `flask --app task_04_flask.py run`
if __name__ == "__main__":
    app.run()
