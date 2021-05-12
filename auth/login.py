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


def complexity(password):
    """Confirms and entered password meets the needed complexity"""
    if (len(password) >= 12
            and any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
            and password_is_not_common(password)):
        return True
    return False


def register_user(username, password):
    """Registers the user"""
    hash_pass = sha256_crypt.hash(password)
    with open('passfile.txt', 'a') as f:
        info = f'{{"username": "{username}", "password": "{hash_pass}"}}'
        f.write(f'\n{info}')


def valid_login(username, password):
    """Checks for a valid login"""
    with open('passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == username:
                return sha256_crypt.verify(password, user['password'])
    return False


def reset_password(username, new_pass, old_pass):
    """Resets a user password"""
    if valid_login(username, old_pass):
        accounts = open('passfile.txt', 'r')
        temp_file = open('temp_file.txt', 'w')
        with accounts, temp_file:
            for record in accounts:
                user = json.loads(record)
                if user['username'] != username:
                    temp_file.write(json.dumps(user) + '\n')
                else:
                    user['password'] = sha256_crypt.hash(new_pass)
                    temp_file.write(json.dumps(user) + '\n')
    return True
                    

def password_is_not_common(password):
    """Check password against a list of common passwords"""
    with open('commonPasswords.txt', 'r') as f:
        for line in f:
            if line == password:
                return False
    return True


def matches_last_password(username, new_pass):
    """Checks for a valid login"""
    with open('passfile.txt', 'r') as f:
        for line in f:
            user = json.loads(line)
            if user['username'] == username:
                return sha256_crypt.verify(new_pass, user['password'])
    return False
