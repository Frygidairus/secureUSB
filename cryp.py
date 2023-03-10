import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

with open('salt.txt', 'rb') as file:
    salt = file.read()

kdf = PBKDF2HMAC(
    algorithm=hashlib.sha256(),
    length=32,
    salt=salt,
    iterations=480000
)

def create_and_store_key(pwd):
    key = base64.urlsafe_b64encode(kdf.derive(pwd))
    print(key)
    with open('myKey.txt', 'wb') as file:
        file.write(hashlib.sha256(key).digest())


def check_key(ukey):
    uhash = hashlib.sha256(ukey).digest()

    with open('myKey.txt', 'rb') as file:
        rhash = file.read()

    if uhash == rhash:
        return True
    else:
        return False

def derive_key(pwd):
    key = base64.urlsafe_b64encode(kdf.derive(pwd))
    return key
# key = create_and_store_key()
# print(key)


def encrypt_file(key, nameOfFile):
    with open(nameOfFile, 'rb') as file:
        original = file.read()

    encoded = Fernet(key).encrypt(original)

    with open(nameOfFile, 'wb') as file:
        file.write(encoded)


def decrypt_file(key, nameOfFile):
    with open(nameOfFile, 'rb') as file:
        original = file.read()

    encoded = Fernet(key).decrypt(original)

    with open(nameOfFile, 'wb') as file:
        file.write(encoded)
