from datetime import datetime, timedelta
from typing import Optional, Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from passlib.context import CryptContext
from app.models.database_manager import DatabaseManager
from app.schemas.pydantic.user import User
from app.dao.address_dao import AddressDao
from app.dao.email_dao import EmailDao



SECRET_KEY = "bcb5d7ffc84c89f5c53302849a03bc6835063b874b21e660b0b74c34c6607e6a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_pass_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)



def get_user_auth(username: str):
    connection = DatabaseManager().get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `Auth` WHERE `username`=%s"
            connection.ping(reconnect=True)
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            return result
    except Exception as e:
        return None
    
def get_user_from_username(username: str):
    connection = DatabaseManager().get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `User` WHERE `user_id` IN (SELECT `user_id` FROM `Auth` WHERE `username`=%s)"
            connection.ping(reconnect=True)
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            return result
    except Exception as e:
        return None

def authenticate_user(username:str, password:str):
    user = get_user_auth(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Authentication",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    
    except JWTError:
        raise credentials_exception
    
    user = get_user_from_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    addresses = AddressDao().get_address_by_id(user["user_id"])
    emails = EmailDao().get_email_by_id(user["user_id"])
    return User(**user, address=addresses, email=emails)