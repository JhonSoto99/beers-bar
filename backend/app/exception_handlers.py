from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.base_exceptions import CustomError
from app.repositories.exceptions import LoadOrderError, LoadStockError
from app.services.exceptions import InvalidOrderDataError


async def handle_custom_error(
    request: Request, exc: CustomError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": str(exc)},
    )


def exception_container(app: FastAPI) -> None:
    app.exception_handler(LoadOrderError)(handle_custom_error)
    app.exception_handler(LoadStockError)(handle_custom_error)
    app.exception_handler(InvalidOrderDataError)(handle_custom_error)
