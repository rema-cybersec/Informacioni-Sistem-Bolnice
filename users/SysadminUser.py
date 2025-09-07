from users.User import User
from config import ADMINS_JSON_PATH, COMPANY_KEY_GPG_PATH
from bcrypt import checkpw
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

    def ValidatePassword(self, admin_data: dict) -> bool:
        if checkpw(self.password.encode('utf-8'), admin_data["password"].encode('utf-8')):
            return True
        return False