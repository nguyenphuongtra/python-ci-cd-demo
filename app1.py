"""Module này chứa Flask app."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Trang chủ trả về chuỗi chào mừng."""
    return "Hello from Flask CI/CD on Heroku!"
