def more_than_20(file):
    words = []
    data = open(file, 'r')
    words = [x.strip() for x in data if len(x.strip()) > 20]
    return words

def has_no_e(word):
    DoesHaveE = False
    for i in word:
        if i == "e" or i == "E":
            DoesHaveE = True
    if DoesHaveE == True:
        return False
    else:
        return True

# def uses_only(word, letters):
#     isTrue = 0
#     for i in word:
#         for j in letters:
#             if j == i:
#                 isTrue += 1
#     if isTrue == len(word):
#         return True
#     else:
#         return False
# print(uses_only("Wolf", "odf"))