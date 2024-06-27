from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError

from app.api.routes import router as status_router
from app.api.routes.words import router as word_router
from app.api.helpers import parse_validation_errors


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError): 
    return parse_validation_errors(exc=exc)

app.include_router(router=status_router, tags=["status"])
app.include_router(router=word_router, prefix="/api", tags=["words"])