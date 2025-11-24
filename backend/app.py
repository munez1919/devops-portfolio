from flask import Flask, jsonify
import os
from database import test_db_connection   # ← переносим сюда

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify(status="ok")

@app.route("/api/ping")
def ping():
    return jsonify(message="pong from backend")

@app.route("/health/db")
def health_db():
    return test_db_connection()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

