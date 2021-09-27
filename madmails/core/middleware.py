"""
This module contains middleware used in our API
"""
from loguru import logger
from starlette.requests import Request

from starlette.responses import Response


async def catch_exceptions_middleware(request: Request, call_next):
    """
    Global exception handler to catch any unexpected exception
    and send a pretty response.

    Args:
        request: is the incoming request injected by FastAPI
        call_next: is the next middleware or endpoint to call. (it's a chain)

    Returns:
        A Response based on the endpoint or a general error message if applicable.
    """
    try:
        return await call_next(request)
    except Exception as err:  # pylint: disable=broad-except
        logger.error("something unexpected happened: {}", err)
        return Response("Internal server error", status_code=500)
