from User import User
from config import ADMINS_JSON_PATH, COMPANY_KEY_GPG_PATH
from bcrypt import checkpw
import json
import base64

class SysadminUser(User):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def LoadSecretKey(self) -> bool:
        with open(COMPANY_KEY_GPG_PATH, 'r') as file:
            self.key = file.read().strip()
            return True
        return False
    
    def CheckSecretKey(self, key: str) -> bool:
        if self.key == None:
            self.LoadSecretKey()
        if self.key.encode('utf-8') == base64.b64encode(key.encode('utf-8')):
            return True
        return False

    def ValidatePassword(self, password: str) -> bool:
        with open(ADMINS_JSON_PATH, 'r') as file:
            data = json.dump(file);
        for admin in data:
            if admin["username"] == self.username:
                if checkpw(password.encode('utf-8'), admin["password"].encode('utf-8')):
                    return True
            else:
                return False
        return False