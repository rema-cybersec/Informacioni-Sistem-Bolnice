from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH
import json

def get_admin_by_username(username: str) -> dict | None:
    with open(ADMINS_JSON_PATH, 'r') as file:
        data = json.load(file)
    for admin in data:
        if admin["username"] == username:
            return admin
    return None

def get_lekar_by_username(username: str) -> dict | None:
    with open(LEKARI_JSON_PATH, 'r') as file:
        data = json.load(file)
    for lekar in data:
        if lekar["username"] == username:
            return lekar
    return None

def get_all_admin_data() -> list:
    with open(ADMINS_JSON_PATH, 'r') as file:
        out = json.load(file)
    return out