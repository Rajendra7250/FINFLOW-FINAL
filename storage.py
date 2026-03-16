# storage.py
import json
from pathlib import Path

# ─────────────────────────────────────────────
# PERSISTENT STORAGE — JSON per user
# ─────────────────────────────────────────────
DATA_DIR = Path("finflow_data")
DATA_DIR.mkdir(exist_ok=True)

def _user_file(username: str) -> Path:
    return DATA_DIR / f"{username}.json"

def load_user_disk(username: str) -> dict:
    f = _user_file(username)
    if f.exists():
        try:
            with open(f, "r", encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            pass
    return _empty_data()

def save_user_disk(username: str, data: dict):
    f = _user_file(username)
    with open(f, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2, default=str)

def _users_file() -> Path:
    return DATA_DIR / "_users.json"

def load_users_disk() -> dict:
    f = _users_file()
    if f.exists():
        try:
            with open(f, "r", encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            pass
    return {
        "admin": {"password": "Admin@123", "name": "Admin User", "color": "#00E5A0"}
    }

def save_users_disk(users: dict):
    f = _users_file()
    with open(f, "w", encoding="utf-8") as fh:
        json.dump(users, fh, ensure_ascii=False, indent=2)