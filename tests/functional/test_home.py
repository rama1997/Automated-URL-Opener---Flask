def test_home_page_get(test_app):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_app.get('/')
    assert response.status_code == 200
    assert b"Home" in response.data

def test_home_page_post(test_app):
    """
    GIVEN a Flask application
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_app.post('/')
    assert response.status_code == 405
    assert b"Flask User Management Example!" not in response.data