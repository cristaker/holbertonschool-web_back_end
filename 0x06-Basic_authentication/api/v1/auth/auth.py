#!/usr/bin/env python3
''' Basic authentication '''
from flask import request
from typing import List, TypeVar


class Auth():
    ''' a class to manage the API authentication '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Define which routes don't need authentication '''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return request