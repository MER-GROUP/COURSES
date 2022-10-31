# авторское решение
a = list(map(int, input().split()))
zayats1 = a[0]
zayats2 = a[1]

if zayats1 > 0 and zayats2 > 0 or zayats1 < 0 and zayats2 < 0:
    print(max(abs(zayats1), abs(zayats2)) * 2)
else:
    if abs(zayats2) > abs(zayats1):
        zmax = abs(zayats2)
        zmin = abs(zayats1)
    else:
        zmax = abs(zayats1)
        zmin = abs(zayats2)
    result = 0
    result += zmin * 2
    result += (zmin * 3 + zmax) * 2
    print(result)