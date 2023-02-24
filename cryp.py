from cryptography.fernet import Fernet


def create_and_store_key():
    key = Fernet.generate_key()
    with open('python/scripts/addOns.txt', 'wb') as file:
        file.write(key)

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
