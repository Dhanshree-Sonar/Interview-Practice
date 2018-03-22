##Write a password generator in Python. Be creative with how you generate
##passwords - strong passwords have a mix of lowercase letters, uppercase letters,
##numbers, and symbols. The passwords should be random, generating a new password
##every time the user asks for a new password.

# Used random to generate random numbers
# Used string module to get letters digits and special characters

import string
import random

def generate_password(strength):
    option = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

    length = 16 if strength == 'strong' else 8

    return "".join(random.sample(option, length))

password = generate_password('strong')
print (password)

password = generate_password('short')
print (password)

password = generate_password('short')
print (password)
