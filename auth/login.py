"""
    Author: Zachary Brandenburg
"""

import json
import string

from passlib.hash import sha256_crypt


def user_exists(uname):
    """Checks if user exists in the passfile"""
    with open('passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == uname:
                return True
        return False


def complexity(pword):
    """Confirms and entered password meets the needed complexity"""
    if (len(pword) >= 12
            and any(c.islower() for c in pword)
            and any(c.isupper() for c in pword)
            and any(c.isdigit() for c in pword)
            and any(c in string.punctuation for c in pword)):
        return True
    return False


def register_user(username, password):
    """Registers the user"""
    hash_pass = sha256_crypt.hash(password)
    with open('passfile.txt', 'a') as f:
        info = f'{{"username": "{username}", "password": "{hash_pass}"}}'
        f.write(f'\n{info}')


def valid_login(username, password):
    """Checks fo a valid login"""
    with open('passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == username:
                return sha256_crypt.verify(password, user['password'])
    print('Password not found')
