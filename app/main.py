from fastapi import FastAPI
from app.api.routes import router as status_router
from app.api.routes.words import router as word_router

app = FastAPI()

app.include_router(router=status_router, tags=["status"])
app.include_router(router=word_router, prefix="/api", tags=["words"])