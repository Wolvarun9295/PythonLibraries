sampleTuple = (1, 2, 3, 4, 1, 2, 2, 3, 4)
print(sampleTuple)
countThis = int(input("Enter a number check it's count: "))
for i in sampleTuple:
    if countThis == i:
        print(f'The count of {countThis} is: {sampleTuple.count(i)}')
        break
