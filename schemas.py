class UserBase(BaseModel):
    login: str

class UserDb(UserBase):
    password: str

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id: int

    class Config:
        from_attributed=True