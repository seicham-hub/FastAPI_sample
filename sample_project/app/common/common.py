from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from typing import Union
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app import models
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def check_permission_for_conversation(user_id: int, conversation_id: int) -> bool:
    users: list = models.get_users_joined_in_conversation(conversation_id)

    for user in users:
        if user.id == user_id:
            return True

    return False


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_public_key():
    with open("/var/www/sample_project/app/public_key_sample.pem", "r") as file:
        public_key = file.read()

    return public_key


def get_private_key():
    with open("/var/www/sample_project/app/private_key_sample.pem", "r") as file:
        private_key = file.read()

    return private_key


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, get_private_key(), algorithm=os.environ["ALGORITHM"]
    )
    return encoded_jwt
