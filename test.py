# import bcrypt
# import base64
from utils.Utils import is_valid_jmbg

# def hash_password(password: str):
#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed

# def b64hash_text(text: str):
#     return base64.b64encode(text.encode("utf-8"))

if __name__ == "__main__":
    print(is_valid_jmbg("3010000800000"))