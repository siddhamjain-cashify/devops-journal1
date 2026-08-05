from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Hello from Docker v2!"}


@app.route("/health")
def health():
    return "OK", 200


@app.route("/whoami")
def whoami():
    return {"hostname": socket.gethostname()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
