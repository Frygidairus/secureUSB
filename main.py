import cryp
from pathlib import Path

'''
   with open('dirEnc/toBeEnc.txt', 'rt') as reader:
      print(reader.read())
   with open('dirEnc/file2.txt', 'rt') as reader:
      print(reader.read())
   with open('dirEnc/file3.txt', 'rt') as reader:
      print(reader.read())
'''

# Retrieve all the file names within the dirEnc folder
def get_all_file_names():
    theFiles = []
    for file in Path('dirEnc').iterdir():
        theFiles.append(file)
    return theFiles



if __name__ == '__main__':

    print('Hello! What do you want to do?\n')
    # Uses the password entered by the user to encrypt data within the dirEnc folder after checking the password is the right one 
    print('a) encrypt\n')
    # Uses the password entered by the user to decrypt data within the dirEnc folder after checking the password is the right one
    print('b) decrypt\n')
    choice = input('c) nothing\n')

    if choice == 'a':
        pwd = bytes(input('Please enter your password: '),'utf-8')
        ukey = cryp.derive_key(pwd)

        if cryp.check_key(ukey):
            theFiles = get_all_file_names()
            for file in theFiles:
                cryp.encrypt_file(ukey, file)
            print('Your files are now encrypted!')
        else:
            print('Wrong password.')

    elif choice == 'b':
        pwd = bytes(input('Please enter your password: '), 'utf-8')
        ukey = cryp.derive_key(pwd)

        if cryp.check_key(ukey):
            theFiles = get_all_file_names()
            for file in theFiles:
                cryp.decrypt_file(ukey, file)
            print('Your files are now decrypted!')
        else:
            print('Wrong password.')
    # Set up the password
    elif choice == 'ini':
        pwd = bytes(input('what is the password to initialize?'),'utf-8')
        cryp.create_and_store_key(pwd)

    else:
        print('ByeBye!')
