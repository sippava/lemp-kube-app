from flask import Flask, jsonify
import os
import mysql.connector
import random

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "mysql"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "root_password"),
        database=os.environ.get("DB_NAME", "test_db"),
    )

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/random")
def random_number():
    return jsonify({"number": random.randint(1, 100)})

