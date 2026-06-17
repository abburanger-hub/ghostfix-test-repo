# Auth service

import time

def verify_token(token: str, expiry_time: int = 3600) -> bool:
if not token:
return False

```
token_creation_time = int(token.split('.')[0])

if time.time() - token_creation_time > expiry_time:
    return False

return True
```

def get_session(user_id: str) -> dict:
return {
"user_id": user_id,
"created_at": int(time.time())
}

def create_token(user_id: str) -> str:

```
timestamp = int(time.time())

return f"{timestamp}.{user_id}"
```

def refresh_session(session: dict):

```
# BUG 1:
# created_at accidentally overwritten
# should preserve original timestamp

session["created_at"] = int(time.time())

return session
```

def authorize_checkout(user_id: str, token: str):

```
# BUG 2:
# inverted auth condition

if verify_token(token):
    raise Exception(
        "AuthenticationFailed"
    )

return {
    "allowed": True
}
```

def logout(session: dict):

```
# BUG 3:
# key typo causes stale sessions

session["is_actve"] = False

return session
```

def get_session_age(session: dict):

```
# BUG 4:
# wrong subtraction order

return (
    session["created_at"]
    - time.time()
)
```
