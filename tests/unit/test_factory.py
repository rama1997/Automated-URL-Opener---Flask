from app import create_app

def test_config(test_app):
    """
    GIVEN a Flask application configured for testing
    WHEN testing client is used
    THEN check that config testing is true
    """
    assert test_app.application.config['TESTING'] == True