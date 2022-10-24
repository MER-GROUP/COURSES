import string
import random

def generate_index():
    return f'{ra()}{ra()}{ri()}_{ri()}{ra()}{ra()}'
    
def ra():
    return random.choice(string.ascii_uppercase)
    
def ri():
    return random.randrange(100)
    
# print(generate_index())
# print(f'{string.ascii_uppercase}')
# print(f'{string.digits}')