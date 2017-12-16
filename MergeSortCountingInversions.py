def merge(arr, l, m, r):
    inv = 0
    i = l
    j = m
    tmp = []
    while i < m and j < r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            inv += m-i
            tmp.append(arr[j])
            j+=1

    tmp += arr[i:m]
    tmp += arr[j:r]

    arr[l:r] = tmp

    return inv


def mergeSort(arr, l, r):
    if r - l == 1:
        return 0

    first = mergeSort(arr, l, (r+l)/2)
    second = mergeSort(arr, (r+l)/2, r)
    return first + second + merge(arr, l, (l+r)/2, r)


def countInversions(arr):
    return mergeSort(arr, 0, len(arr))


if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = countInversions(arr)
        print result
