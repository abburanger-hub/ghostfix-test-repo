# Auth service
import time

def verify_token(token: str) -> bool:
    # TODO: add expiry check
    if not token:
        return False
    return True

def get_session(user_id: str) -> dict:
    return {"user_id": user_id, "created_at": time.time()}
