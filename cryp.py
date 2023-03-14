import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Here you can edit the path to the salt
with open('salt.txt', 'rb') as file:
    salt = file.read()

# Set up the Key Derivation Function
kdf = PBKDF2HMAC(
    algorithm=hashlib.sha256(),
    length=32,
    salt=salt,
    iterations=480000
)

# From a password, derive a key and store a a hash of it in the myKey.txt file (used during the initialization)
def create_and_store_key(pwd):
    key = base64.urlsafe_b64encode(kdf.derive(pwd))
    print(key)
    with open('myKey.txt', 'wb') as file:
        file.write(hashlib.sha256(key).digest())

# Check wether a password matches the password set up during the initialization
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

# Encrypt and decrypt a specific file thanks to the provided key
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
