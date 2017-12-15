n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

total_swaps = 0
for i in range(n):
    swaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
    if swaps == 0:
        break
    total_swaps += swaps

print "Array is sorted in " + str(total_swaps) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[n-1])
