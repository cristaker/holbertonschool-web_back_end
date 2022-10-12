#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:
    """
    Class DB
    """

    def __init__(self):
        """ Init
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user to DB
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """ 2. Find user by
        """
        results = self._session.query(User).filter_by(**kwargs)
        return results.one()

    def update_user(self, user_id: int, **kwargs: dict):
        """ 2. Update user
        """

        user = self.find_user_by(id=user_id)

        for k, _ in kwargs.items():
            if k not in list(user.__dict__.keys()):
                raise ValueError()

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.add(user)
        self._session.commit()