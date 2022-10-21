from fastapi import FastAPI
from routes import eval_router

app = FastAPI()
app.include_router(eval_router, prefix="/api/v1")


@app.get("/")
@app.get("/index")
async def root():
    return "Hello, world!"
