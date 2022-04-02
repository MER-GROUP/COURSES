from string import ascii_uppercase as s
from random import randrange as r
from random import choice as c

def generate_index():
    return f'{c(s)}{c(s)}{r(100)}_{r(100)}{c(s)}{c(s)}'
    
print(generate_index())