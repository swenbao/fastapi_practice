# Data validation
# Request body & Response body
# most of the time server will return the response body
# but client don't have to send the request body
# to send the request body, use POST, PUT, DELETE, PATCH methods
# send the request body with GET method has undefined behavior, but is supported by FastAPI in extreme use cases

from fastapi import FastAPI
from pydantic import BaseModel # pydantic is a data validation library
# pydantic has more advance validation:
from pydantic import EmailStr # EmailStr validate email format
from pydantic import conint # conint validate integer range
from pydantic import constr # constr validate string format, support regex
from pydantic import field_validator # field_validator validate field value

class User(BaseModel):
    name: constr(regex=r'^[a-zA-Z0-9_.-]+$') # name must be alphabet only
    email: str
    age: conint(gt=0, lt=150) # age must be greater than 0 and less than 100

    # Custom validation
    @field_validator('username')
    def username_must_not_contain_spaces(cls, v):
        if ' ' in v:
            raise ValueError('username must not contain spaces')
        return v
    

app = FastAPI()

@app.post("/register/")
async def register_user(user: User):
    return user
