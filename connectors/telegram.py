"""Telegram adapter skeleton using Bot API."""
import os, httpx

async def get_me():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        return {"connected": False, "reason": "missing_credentials"}
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(f"https://api.telegram.org/bot{token}/getMe")
        r.raise_for_status()
        return {"connected": True, "bot": r.json()}
