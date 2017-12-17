ways = [0, 1, 2, 4]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    while len(ways) < n + 1:
        i = len(ways)
        ways.append(ways[i-1] + ways[i-2] + ways[i-3])        
    print ways[n]
