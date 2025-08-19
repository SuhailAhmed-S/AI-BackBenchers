# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users[data['username']] = data
    return jsonify({"msg": "User registered successfully"})

@app.route('/progress/<username>', methods=['GET'])
def get_progress(username):
    return jsonify(users.get(username, {"msg": "User not found"}))

if __name__ == '__main__':
    app.run(debug=True)
