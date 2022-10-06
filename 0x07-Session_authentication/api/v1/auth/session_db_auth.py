#!/usr/bin/env python3
"""
SessionDBAuth module for the API
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
import uuid


class SessionDBAuth(SessionExpAuth):
    """ SessionAuth
    """

    def create_session(self, user_id=None):
        """ Create a session
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        user_session = UserSession()
        user_session.user_id = user_id
        user_session.session_id = session_id
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ returns the User ID by requesting UserSession in
            the database based on session_id
        """
        if type(session_id) is not str:
            return None
        try:
            users_sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None

        if len(users_sessions) == 0:
            return None

        user_session = users_sessions[0]

        if self.session_duration <= 0:
            return user_session.user_id

        created_at_session = user_session.created_at

        duration_session = created_at_session + timedelta(
            seconds=self.session_duration
        )

        if duration_session < datetime.now():
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """ destroys the UserSession based on the Session ID from
            the request cookie
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if not session_id:
            return False

        try:
            users_sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None

        if len(users_sessions) == 0:
            return None

        user_session = users_sessions[0]
        user_session.remove()

        return True