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
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object
        """
        return None
