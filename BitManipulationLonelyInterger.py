def lonely_integer(a):
    res = 0
    for elem in a:
        res ^= elem
    return res
    
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a
