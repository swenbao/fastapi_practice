from fastapi import FastAPI

app = FastAPI()

# HTTP methods

# GET: read data
@app.get("/")
def read_root():
    return {"Hello": "World"}

# POST: create data
@app.post("/items/")
def create_item(name: str, price: float):
    return {'name': name, 'price': price}

# PUT: update data
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {'item_id': item_id, 'name': name, 'price': price}

# DELETE: delete data
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {'message': f'Item {item_id} has been deleted'}

# Path parameter
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/items/{item_name}")
def read_item(item_name:str):
    return {"item_name": item_name}

# query parameter
# http://127.0.0.1:8000/testQ/?item_id=1234&item_name=sdajfl
@app.get("/testQ/")
def read_item(item_id: int, item_name: str):
    return {"item_id": item_id, "item_name": item_name}

# optional query parameter
# http://127.0.0.1:8000/testOQ/1234/details?include_email=True
@app.get("/testOQ/{user_id}/details")
def read_item(user_id: int, include_email:bool = False):
    if include_email:
        return {"user_id": user_id, "include_email": "True"}
    else:
        return {"user_id": user_id, "include_email": "False"}
