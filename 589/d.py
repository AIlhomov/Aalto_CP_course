word1 = input()
word2 = input()
diffIndexes = []
for i in range(len(word1)):
    if word1[i] != word2[i]:
        diffIndexes.append(i)

print(diffIndexes)