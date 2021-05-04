import json
import string

from passlib.hash import sha256_crypt


def user_exists(username):
    with open('../passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == username:
                return True
        return False


def complexity(password):
    if (len(password) >= 8
            and any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
        return True
    return False


def register_user(username, password):
    hash_pass = sha256_crypt.hash(password)
    with open('../passfile.txt', 'a') as f:
        info = f'{{"username": "{username}", "password": "{hash_pass}"}}'
        f.write(f'\n{info}')


def valid_login(username, password):
    with open('../passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == username:
                return sha256_crypt.verify(password, user['password'])
    print('Password not found')
