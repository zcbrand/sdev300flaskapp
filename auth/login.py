import json

from passlib.hash import sha256_crypt


def user_exists(username):
    with open('passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == username:
                return True
        return False


def add_user_pass(username, password):
    hash_pass = sha256_crypt.hash(password)
    with open('passfile.txt', 'a') as f:
        info = f'{{"username": "{username}", "password": "{hash_pass}"}}'
        f.write(f'\n{info}')


def valid_login(username, password):
    hash_pass = sha256_crypt.hash(password)
    with open('passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == username:
                return sha256_crypt.verify(password, user['password'])
    print('Password not found')

