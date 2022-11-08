def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the user_email and user__password fields are defined correctly
    """
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.password == 'FlaskIsAwesome'

def test_new_note(new_note):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the user_email and user__password fields are defined correctly
    """
    assert new_note.title == 'patkennedy79@gmail.com'
    assert new_note.url == 'https://www.youtube.com/'
    assert new_note.frequency == 'Weekly'
    assert new_note.days == 'Tuesday'
    assert new_note.month == 'January'
