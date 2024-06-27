
from fastapi.exceptions import RequestValidationError
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def parse_validation_errors(exc: RequestValidationError):
    message = []
    for error in exc.errors(): 
        print(error)
        message.append(error.pop('msg') + f': {error["loc"][1]}')

    return JSONResponse(content=jsonable_encoder({"error": message}), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)