#!/usr/bin/env python3
"""
Template for authentication system
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Authentification methods
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object
        """
        return None
