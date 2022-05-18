s = input()

for i in range(1, len(s)+1):
    if len(s) % i == 0 and s[i:] == s[:i] * ( (len(s) - i) // i ):
        print(len(s) // i)
        break