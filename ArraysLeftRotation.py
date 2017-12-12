def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        
def shifted_index(i, k, n):
    return (i - k) % n

def array_left_rotation(a, n, k):
    for cycle_number in range(gcd(n, k)):
        i = cycle_number
        j = shifted_index(i, k, n)
        tmp = a[j]
        a[j] = a[i]
        i = j
        while i != cycle_number:
            j = shifted_index(i, k, n)
            tmp, a[j] = a[j], tmp
            i = j
    return a
      
n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
