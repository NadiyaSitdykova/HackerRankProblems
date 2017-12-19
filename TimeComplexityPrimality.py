def isPrime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for p in range(3, int(n**0.5) + 1, 2):
        if n % p == 0:
            return False
    return True

m = int(raw_input().strip())
for _ in xrange(m):
    n = int(raw_input().strip())
    if isPrime(n):
        print "Prime"
    else:
        print "Not prime"
