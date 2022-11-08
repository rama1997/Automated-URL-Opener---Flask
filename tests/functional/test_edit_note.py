from flask_login import current_user
import test_auth
import test_add_note

def test_edit_note_get(test_app, new_note):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/edit_note' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_app.get('/edit_note?note=1')
    assert response.status_code == 200
    assert b"Edit Link" in response.data

def test_edit_note_post(test_app, new_note, new_user):
    """
    GIVEN a Flask application
    WHEN the '/'edit_note page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    test_add_note.test_add_note_post(test_app,new_note)
    response = test_app.post('/edit_note', data={
        "url": "https://www.youtube.com/feed/subscriptions",
        "title": "Youtubetrf",
        "frequency": "Daily",
        "days": "5",
        "month": "March",
        "note_id": 1,
    }, follow_redirects=True)
    assert response.status_code == 200