from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello Johir!",
        "status": "Server is working"
    }
