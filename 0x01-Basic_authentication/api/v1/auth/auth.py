#!/usr/bin/env python3

"""Module of Index views"""

from typing import List, TypeVar
from flask import request


class Auth:
    '''Class method'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Public method for our class'''
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        '''Method to return none rqs'''
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        '''Method for current user'''

        return None
