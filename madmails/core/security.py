from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseSettings
from starlette import status


class ApiSecuritySettings(BaseSettings):
    """
    This model is used to configure the security of madmails API
    """
    api_key: str

    class Config:
        env_prefix = 'ngx_'


_DEFAULT_SECURITY_SETTINGS = ApiSecuritySettings()
_DEFAULT_API_KEY_HEADER = APIKeyHeader(name="NGX-API-KEY")


def verify_api_key(api_key_header: str = Security(_DEFAULT_API_KEY_HEADER)) -> None:
    """
    Verify that the environment variable NGX_API_KEY value is the same as the one passed in the header.
    This ultra simple way of securing the endpoints need to be replaced by something more robust.

    Args:
        api_key_header: is the value of the header NGX-API-KEY

    Raises:
        HTTPException: with code 401 if the keys are different
    """
    if api_key_header != _DEFAULT_SECURITY_SETTINGS.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
