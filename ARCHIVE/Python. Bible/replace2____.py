s = input()
old = s[s.find('h') : s.rfind('h') + 1]
#old2 = s[s.rfind('h') : s.find('h') -1 : -1]
new = old[ : : -1]
#print(old)
#print(old2)
#print(new)
print(s.replace(old, new))