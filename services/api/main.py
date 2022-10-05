import uvicorn
from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def home():
#     return {"Hello": "World"}

# @app.get("/")
# def home():
#     return {"Hello": "GET"}

@app.post("/")
def home_post(text: str):
    return {"Hello": text}

# @app.route("/employee/<int:id>/")
# def home():
#     return {"id": id}

@app.post("/employee")
def home(department: str):
    return {"department": department}

if __name__ == "__main__":
    uvicorn.run("hello_world_fastapi:app")
