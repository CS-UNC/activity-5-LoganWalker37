def more_than_20(file):
    words = []
    data = open(file, 'r')
    words = [x.strip() for x in data if len(x.strip()) > 20]
    return words

def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

def uses_only(word, letters):
    successes = 0
    for i in word:
        for j in letters:
            if j == i:
                successes += 1
    if successes == len(word):
        return True
    else:
        return False

def uses_only(word, letters):
    for value in word:
        if value not in letters:
            return False
    return True
        
        
    
# def all_uses_only(file, letters):
#     words = []
#     data = open(file, 'r')
#     words = [x.strip() for x in data if uses_only(file, letters) == True]
#     return words
print(uses_only("aa", "abrd"))
