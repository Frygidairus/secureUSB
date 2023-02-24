import python.scripts.cryp as cryp
from pathlib import Path


'''
   with open('dirEnc/toBeEnc.txt', 'rt') as reader:
      print(reader.read())
   with open('dirEnc/file2.txt', 'rt') as reader:
      print(reader.read())
   with open('dirEnc/file3.txt', 'rt') as reader:
      print(reader.read())
'''

def get_all_file_names():
   theFiles = []
   for file in Path('dirEnc').iterdir():
      theFiles.append(file)
   return theFiles



if __name__ == '__main__':

   print('Hello! What do you want to do?\n')
   print('a) encrypt\n')
   print('b) decrypt\n')
   choice = input('c) nothing\n')

   if choice == 'a':
      key = cryp.create_and_store_key()
      theFiles = get_all_file_names()
      for file in theFiles:
         cryp.encrypt_file(key, file)

   elif choice == 'b':
      with open('myKey.txt', 'rb') as reader:
         key = reader.read()
      theFiles = get_all_file_names()
      for file in theFiles:
         cryp.decrypt_file(key, file)

   else:
      print('ByeBye!')
