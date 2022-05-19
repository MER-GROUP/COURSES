def unpack(it):
    out = ''
    dig = ''
    for v in it:
        if v == ')':
            break
        elif v == '(':
            out += unpack(it) * int(dig if dig else 1)
            dig = ''
        elif v.isdigit():
            dig += v
        else:
            out += v
    return out 
        
print(unpack(iter(input())))