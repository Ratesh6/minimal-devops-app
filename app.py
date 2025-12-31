import os
import sys
from flask import Flask, jsonify

APP_NAME = "minimal-devops-app"
PORT = os.getenv("APP_PORT")

if not PORT:
    print("ERROR: APP_PORT environment variable is not set", file=sys.stderr)
    sys.exit(1)

PORT = int(PORT)

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "app_name": APP_NAME,
        "listening_port": PORT
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
