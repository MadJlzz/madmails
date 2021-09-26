"""
This module is the entrypoint of the project.
It runs a FastAPI webserver with uvicorn.
"""
import uvicorn
from fastapi import FastAPI
from loguru import logger
from starlette.requests import Request
from starlette.responses import Response

from madmails.controller import mail

# Initialization of a new FastAPI app
app = FastAPI(title="MadMails", description="A developer friendly service for sending mails.", version="0.1.0")


# Global exception handler to catch any unexpected exception
# and send a pretty response.
@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as err:  # pylint: disable=broad-except
        logger.error("something unexpected happened: {}", err)
        return Response("Internal server error", status_code=500)


# Inclusion of new routers. Same as Flask blueprints.
app.include_router(mail.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, log_level="info")
