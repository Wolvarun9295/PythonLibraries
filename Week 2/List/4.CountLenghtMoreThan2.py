sampleList = ['abc', 'xyz', 'aba', '1221', 'abababa']
count = 0
for word in sampleList:
    if len(word) > 1 and word[0] == word[-1]:
        count += 1
print(f'There are total {count} words greater than 2')
