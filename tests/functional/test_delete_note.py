from flask import jsonify
import json
from flask_login import current_user
import test_auth
import test_add_note

def test_delete_note(test_app, new_note):
    """
    GIVEN a Flask application
    WHEN the '/'delete-note page is posted to (POST)
    THEN check that a '200' status code is returned
    """
    test_add_note.test_add_note_post(test_app,new_note)
    response = test_app.post('/delete-note', json={
        "noteId": new_note.id,
    }, follow_redirects=True)
    assert response.status_code == 200

def test_delete_all_note(test_app, new_note):
    """
    GIVEN a Flask application
    WHEN the '/'delete_all_note page is posted to (POST)
    THEN check that a '200' status code is returned
    """
    test_auth.test_log_in_post(test_app)
    response = test_app.post('/delete_all_notes')
    assert response.status_code == 200