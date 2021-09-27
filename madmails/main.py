"""
This module is the entrypoint of the project.
It runs a FastAPI webserver with uvicorn.
"""
import uvicorn
from fastapi import FastAPI, Depends
from starlette.middleware.base import BaseHTTPMiddleware

from madmails.controller import mail
from madmails.core.middleware import catch_exceptions_middleware
from madmails.core.security import verify_api_key

# Initialization of a new FastAPI app
app = FastAPI(title="MadMails",
              description="A developer friendly service for sending mails.",
              version="0.1.0",
              dependencies=[Depends(verify_api_key)])

# Middlewares configuration
app.add_middleware(BaseHTTPMiddleware, dispatch=catch_exceptions_middleware)

# Inclusion of new routers. Same as Flask blueprints.
app.include_router(mail.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, log_level="info")
