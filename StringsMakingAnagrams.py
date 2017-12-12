def get_frequencies(s):
    freq = [0 for _ in range(26)]
    for c in s:
        freq[ord(c) - ord('a')] += 1
    return freq

def number_needed(a, b):
    freq_a = get_frequencies(a)
    freq_b = get_frequencies(b)
    difference = 0
    for i in range(26):
        difference += abs(freq_a[i] - freq_b[i])
    return difference    

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
