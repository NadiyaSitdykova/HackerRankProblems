def binary_search(a, l, r, x):
    while r - l > 1:
        mid = (r + l) / 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            l = mid
        else:
            r = mid
    return -1

def choose_flavors(m, n, a):
    ids = range(n)
    ids = [x for _, x in sorted(zip(a, ids))]
    a = sorted(a)
    for first in range(n):
        second = binary_search(a, first, n, m-a[first])
        if second != -1:
            if ids[first] > ids[second]:
                ids[first], ids[second] = ids[second], ids[first]
            return [ids[first]+1, ids[second]+1]
    return [-1, -1]

t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    flavors = choose_flavors(m, n, a)
    print str(flavors[0]) + " " + str(flavors[1])
