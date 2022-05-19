import re

s = input()
s = s.replace("(", "*('")
s = s.replace(")", "')+'")
#s = "hi2*('priv3*('d3*('i')+'dd')+'qq')+'b0*('pr')+'qwqdd"
lst = s.split('*')
match = re.findall(r'\d+', s)

for ind, el in enumerate(lst[:-1]):
    num = match[ind]
    num_ind = len(num)
    lst[ind] = f"{el[:-num_ind]}'+{num}"
    
s = '*'.join(lst)
eval(f"print('{s}')")