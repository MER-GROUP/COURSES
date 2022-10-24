from random import randrange as r

def generate_ip():
    return '.'.join([str(r(256)) for _ in range(4)])
    
print(generate_ip())