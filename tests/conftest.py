import pytest
from django.utils import translation
from task_manager.users.models import User


@pytest.fixture(scope='module', autouse=True)
def language():
    return translation.activate('en')


@pytest.fixture
def test_users(db):
    return {
        'user1': User.objects.create_user(
            username = 'testuser1',
            password = 'testpassword',
            first_name = 'test',
            last_name = 'user',
        ),
        'user2': User.objects.create_user(
            username='testuser2',
            password='testpassword',
            first_name='test',
            last_name='user',
        )
    }


@pytest.fixture
def test_user1_data():
    return {
        'username': 'testuser1',
        'first_name': 'test',
        'last_name': 'user',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
