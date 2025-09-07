import bcrypt

def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

if __name__ == "__main__":
    print(hash_password("test").decode('utf-8'))