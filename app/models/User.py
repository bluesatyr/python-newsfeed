import bcrypt
from typing import Collection
from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

salt = bcrypt.gensalt()

# a User class that inherits from the Base class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

    # sqlalchemy validation decorator
    @validates('email')
    # add new validate_email() method to the class that a @validates('email') decorator wraps
    def validate_email(self, key, email):
        # make sure email address contains @ character
        assert '@' in email

        return email
    
    @validates('password')
    def validate_password(self, key, password): 
        assert len(password) > 4

        # encrypt password
        return bcrypt.hashpw(password.encode('utf-8'), salt)