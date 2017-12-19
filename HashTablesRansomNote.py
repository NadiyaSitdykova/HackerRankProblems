def ransom_note(magazine, ransom):
    words = {}
    for word in magazine:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for word in ransom:
        if word not in words or words[word] == 0:
            return False
        else:
            words[word] -= 1
    return True
    
m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
