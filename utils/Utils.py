from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH
import os
import base64
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

def get_all_lekar_data() -> list:
    with open(LEKARI_JSON_PATH, 'r') as file:
        out = json.load(file)
    return out

def derive_key(secret_key: str, salt: bytes, iterations: int = 1000, key_length: int = 32) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_length,
        iterations=iterations,
        salt=salt,
        backend=default_backend
    )
    return kdf.derive(secret_key.encode("utf-8"))


def encrypt_data(data:str, secret_key: str, salt: bytes = None):
    if salt is None:
        salt = os.urandom(16)
    aes_key = derive_key(secret_key, salt)
    nonce = os.urandom(12)

    encryptor = Cipher(
        algorithms.AES(aes_key),
        modes.GCM(nonce),
        backend=default_backend
    ).encryptor()

    encrypted_data = encryptor.update(data.encode("utf-8")) + encryptor.finalize()
    return {
        "data" : base64.b64encode(encrypted_data).decode("utf-8"),
        'salt': base64.b64encode(salt).decode("utf-8"),
        'nonce': base64.b64encode(nonce).decode("utf-8"),
        'tag': base64.b64encode(encryptor.tag).decode("utf-8")
    }

def decrypt_data(encrypted_data: dict, secret_key: str) -> str:
    data = base64.b64decode(encrypted_data['data'])
    salt = base64.b64decode(encrypted_data['salt'])
    nonce = base64.b64decode(encrypted_data['nonce'])
    tag = base64.b64decode(encrypted_data['tag'])

    aes_key = derive_key(secret_key, salt)

    decryptor = Cipher(
        algorithms.AES(aes_key),
        modes.GCM(nonce, tag),
        backend=default_backend()
    ).decryptor()

    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return decrypted_data.decode("utf-8")
