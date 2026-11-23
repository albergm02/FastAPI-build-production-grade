from fastapi import Header, HTTPException

# in production, you add this in .env

API_KEY = "your_api_key_here"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key