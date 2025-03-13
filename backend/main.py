from fastapi import FastAPI
from api.routes import router
import uvicorn

app = FastAPI(title="Agno API", version="1.0.0")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to Agno API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
