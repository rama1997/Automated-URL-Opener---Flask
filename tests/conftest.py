from app.models import User, Note
from app import create_app
import pytest

@pytest.fixture(scope='module')
def new_user():
    user = User(email = 'patkennedy79@gmail.com', password = 'FlaskIsAwesome')
    return user

@pytest.fixture(scope='module')
def new_note():
    note = Note(title = 'patkennedy79@gmail.com', url = 'https://www.youtube.com/', frequency = 'Weekly', days = 'Tuesday', month = 'January', id = 1)
    return note

@pytest.fixture(scope='session')
def test_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_app:
        # Establish an application context
        with app.app_context():
            yield test_app # Means that execution is passed to the test functions, where testing will happen