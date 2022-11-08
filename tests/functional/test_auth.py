from flask_login import current_user
from app.extensions import db
from app.models import User, Note
import random

def test_sign_up_get(test_app):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/sign-up' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_app.get('/sign-up')
    assert response.status_code == 200
    assert b"Sign Up" in response.data

def test_sign_up_post(test_app):
    """
    GIVEN a Flask application
    WHEN the '/sign-up' page is posted to (POST)
    THEN check that the response is valid
    """
    rand = random.randint(0, 100000)
    response = test_app.post('/sign-up', data={
        "email": "{}@gmail.com".format(rand),
        "password1": "123",
        "password2": "123",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == "/"

def test_log_in_get(test_app):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_app.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data


def test_log_in_post(test_app):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check that the response is valid
    """
    test_sign_up_post(test_app)
    response = test_app.post('/login', data={
        "email": "test@gmail.com",
        "password": "123",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == "/"


def test_logout(test_app):
    """
    GIVEN a Flask application
    WHEN the '/logout' page is accessed
    THEN check that the response is valid
    """
    response = test_app.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/login"