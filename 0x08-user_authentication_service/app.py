#!/usr/bin/env python3
""" Auth class """
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    """ Takes in a password and returns a salted hash.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """ Returns a string representation of a new UUID
    """
    return str(uuid.uuid4())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initailizes instance of DB
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Returns a User object, or ValueError with a message
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
