from app import add
from app1 import app


def test_add():
    """Test hàm add."""
    assert add(1, 2) == 3


def test_home():
    """Test trang chủ."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data == b'Hello from Flask CI/CD on Heroku!'
