from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_pass_hash(password: str):
    return pwd_context.hash(password)