from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correctName = "admin"
    correctPassword = "password"
    if credentials.username != correctName or credentials.password !=correctPassword:
        raise HTTPException(status_code=401,detail="unauthorized")
    return True