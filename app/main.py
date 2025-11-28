from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router

app = FastAPI(title="AI Study Assistant API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["ALLOWED_ORIGINS"],  
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Study Assistant API"}






