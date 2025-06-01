from . import crud
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import *
from models import *
from schemas import *

app = FastAPI()
models.Base.metadata.create_all(bind = engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/create_user")
def create_user(user : UserCreate, db:Session = Depends(get_db)):
    return create_user(db,user)

@app.get("/user/{user_id}")
def read_user(user_id : int, db:Session = Depends(get_db)):
    user=get_user(db,user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@app.get("/users")
def read_users(db: Session= Depends(get_db)):
    return get_all_users(db)
@app.post("/token")
async def token_get(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_data = user_data.get(form_data.login)
    if not user_data:
        raise HTTPException(status_code = 400 , detail='incorect login or password')
    else:
        user = crud.authenticate_user(db, form_data.user_name, form_data.password)
    if not user:
        raise HTTPException(status_code = 401, detail='incorect username or password')
        token = token_create(data={'sub':user.login})
    return {'access_token': token, "token_type":"bearer"}

@app.get('/protected')
async def protected(token: Annotated[str, Depends(oauth2_scheme)]):
    return{"msg": user.login + " welcome!"}

