from flask import Flask

Tester_app = Flask(__name__)

@Tester_app.route("/")
def home():
    return "Hello, Flask!"
