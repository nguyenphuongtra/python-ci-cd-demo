"""Module này chứa Flask app."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Trang chủ trả về chuỗi chào mừng."""
    return "Hello from Flask CI/CD on DockerHub!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)