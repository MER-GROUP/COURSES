import itertools

'''
def primes(x):
    for chislo in range(2, x + 1):
        cnt = int()
        for i in range(1, chislo + 1):
            if 0 == chislo % i:
                cnt += 1
        if 2 == cnt:
            yield i
                
for i in primes(31):
    print(i)
'''

def primes():
    chislo = 2
    while True:
        cnt = int()
        for i in range(1, chislo + 1):
            if 0 == chislo % i:
                cnt += 1
        if 2 == cnt:
            yield chislo
        chislo += 1
    
print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]