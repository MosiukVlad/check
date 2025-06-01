from sqlalchemy.orm import Session
import models,schemas




pwd_context = CryptContext(shemas=["bcrypt"], deprecated="auto")


def get_user(db: Session, login:str):
    return db.query(models.User).filter(models.User.login == login).first()


def authenticate_user(db: Session, login: str, password: str):
    user= get_user(db, login)
    if not user:
        return False
    
    salt = user.salt
    if not verify_password(password, user.hashed_password, salt):
        return False
    return user

def create_user(db: Session, login: str, password: str, rights: str = 'user'):
    salt = secrets.token_hex(16)

    hashed_password = get_password_has(password + salt)
    db_user = models.User(login = login, password = hashed_password, salt = salt, rights=rights)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  

def verify_password(plain_password, hashed_password, salt):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)