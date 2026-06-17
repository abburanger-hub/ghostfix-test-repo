
# Auth service

import time

def verify_token(token: str, expiry_time: int = 3600) -> bool:
    if not token:
        return False

    # token_creation_time = int(token.split('.')[0])
    token_creation_time = int(token.split('.')[0])

    if time.time() - token_creation_time > expiry_time:
        return False

    return True


def get_session(user_id: str) -> dict:
    return {
        "user_id": user_id,
        "created_at": int(time.time())
    }


def create_token(user_id: str) -> str:

    timestamp = int(time.time())

    return f"{timestamp}.{user_id}"


def refresh_session(session: dict):

    # preserve original timestamp
    session["refreshed_at"] = int(time.time())

    return session


def authorize_checkout(user_id: str, token: str):

    # correct auth condition
    if not verify_token(token):
        raise Exception(
            "AuthenticationFailed"
        )

    return {
        "allowed": True
    }


def logout(session: dict):

    # correct key
    session["is_active"] = False

    return session


def get_session_age(session: dict):

    # correct subtraction order
    return (
        time.time()
        - session["created_at"]
    )
