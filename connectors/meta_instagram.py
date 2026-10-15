"""Instagram Business adapter skeleton. Use only official Meta Graph API credentials."""
import os, httpx

GRAPH = "https://graph.facebook.com/v24.0"

async def account_info():
    token = os.getenv("META_ACCESS_TOKEN")
    user_id = os.getenv("META_IG_USER_ID")
    if not token or not user_id:
        return {"connected": False, "reason": "missing_credentials"}
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(f"{GRAPH}/{user_id}", params={"fields":"id,username", "access_token":token})
        r.raise_for_status()
        return {"connected": True, "account": r.json()}
