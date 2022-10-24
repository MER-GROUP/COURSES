from random import randint

def generate_ip():
    ip = [(str(randint(0, 255)) + '.') for _ in range(4)]
    return ''.join(ip)[: -1]
    
# print(generate_ip())