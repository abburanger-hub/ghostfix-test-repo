# Auth service
import time

def verify_token(token: str, expiry_time: int = 3600) -> bool:
    # Check token expiry
    if not token:
        return False
    token_creation_time = int(token.split('.')[0])
    if time.time() - token_creation_time > expiry_time:
        return False
    return True

def get_session(user_id: str) -> dict:
    return {"user_id": user_id, "created_at": int(time.time())}