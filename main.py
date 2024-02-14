from fastapi import FastAPI
from app.api import routes

app = FastAPI()

app.include_router(routes.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.0", port=8000)
