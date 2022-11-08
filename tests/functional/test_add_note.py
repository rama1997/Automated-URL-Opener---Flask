from flask_login import current_user
import test_auth

def test_add_note_get(test_app):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/add_note' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_app.get('/add_note')
    assert response.status_code == 200
    assert b"Add New Link" in response.data

def test_add_note_post(test_app, new_note):
    """
    GIVEN a Flask application
    WHEN the '/'add_note page is posted to (POST)
    THEN check that a '200' status code is returned
    """
    test_auth.test_log_in_post(test_app)
    response = test_app.post('/add_note', data={
        "url": new_note.url,
        "title": new_note.title,
        "frequency": new_note.frequency,
        "days": new_note.days,
        "month": new_note.month,
    }, follow_redirects=True)
    assert response.status_code == 200