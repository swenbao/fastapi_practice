from fastapi import FastAPI, Form, File, UploadFile

# 2/10 原本看不好

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "message": "Login successful"}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/savefiles/")
async def save_files(file: UploadFile = File(...)):
    with open(f'./upload/{file.filename}', 'wb') as f:
        f.write(file.file.read())

    return {"message": f"{file.filename} saved successfully"}

# multiple files
@app.post("/multiplefiles/")
async def multiple_files(files: list[UploadFile] = File(...)):
    for file in files:
        with open(f'./upload/{file.filename}', 'wb') as f:
            f.write(file.file.read())

    return {"message": f"{len(files)} files saved successfully"}