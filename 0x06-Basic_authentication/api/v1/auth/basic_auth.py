#!/usr/bin/env python3
"""
Auth module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
import binascii
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header for a
            Basic Authentication
        """
        if authorization_header is None or \
           type(authorization_header) is not str or \
           authorization_header[:6] != 'Basic ':
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Returns the decoded value of a Base64
            string base64_authorization_header
        """
        if base64_authorization_header is None or \
           type(base64_authorization_header) is not str:
            return None

        try:
            base64_authorization_header = base64.b64decode(
                                            base64_authorization_header
                                          )
        except binascii.Error:
            return None

        return base64_authorization_header.decode('utf-8')

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """ Returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or \
           type(decoded_base64_authorization_header) is not str or \
           ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            user_credentials = decoded_base64_authorization_header.split(':')
            return user_credentials[0], ':'.join(user_credentials[1:])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password,
            otherwise None
        """
        if user_email is None or type(user_email) is not str or \
           user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = User.search({'email': user_email})
        except KeyError:
            return None

        if len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ retrieves the User instance for a request,
            otherwise None
        """
        authorization_header = self.authorization_header(request=request)
        extract_base64_authorization_header = (
            self.extract_base64_authorization_header(authorization_header)
        )
        decode_base64_authorization_header = (
            self.decode_base64_authorization_header(
                extract_base64_authorization_header
            )
        )
        extract_user_credentials = self.extract_user_credentials(
            decode_base64_authorization_header
        )
        user_object_from_credentials = self.user_object_from_credentials(
            user_email=extract_user_credentials[0],
            user_pwd=extract_user_credentials[1]
        )
        return user_object_from_credentials
    