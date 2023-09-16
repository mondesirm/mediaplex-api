from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from mediaplex.config.authtoken import verify_token

oauth2_scheme = OAuth2PasswordBearer('/login/auth')

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, 'Could not validate credentials', { 'WWW-Authenticate': 'Bearer' })
    return verify_token(credentials_exception, token)