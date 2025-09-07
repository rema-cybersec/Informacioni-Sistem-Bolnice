import bcrypt
import base64

def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def b64hash_text(text: str):
    return base64.b64encode(text.encode("utf-8"))

if __name__ == "__main__":
    print(b64hash_text("testkey").decode("utf-8"))