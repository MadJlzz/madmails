"""
This module is the entrypoint of the project.
It runs a FastAPI webserver with uvicorn.
"""
import uvicorn
from fastapi import FastAPI

from madmails.controller import mail

# Initialization of a new FastAPI app
app = FastAPI(title="MadMails", description="A developer friendly service for sending mails.", version="0.1.0")

# Inclusion of new routers. Same as Flask blueprints.
app.include_router(mail.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, log_level="info")
