from app.sessions.models.users import User
from tests.sessions.models.create_users import create_name


def a_user():
    return UserBuilder()


class UserBuilder:
    def __init__(self):
        self.name = create_name()

    def with_name(self, name):
        self.name = name
        return self

    def build(self):
        return User(self.name)
