from cryptography.fernet import Fernet
from getpass import getpass

def login():
    user = input('Username: ')
    password = getpass('Password: ')

    bpass = bytes(password, 'utf-8')
    key = Fernet.generate_key()
    f = Fernet(key)

    password_crypted = f.encrypt(bpass)
    
    return (f, user, password_crypted)

def decrypt(f, text):
    return (str(f.decrypt(text), 'utf-8'))