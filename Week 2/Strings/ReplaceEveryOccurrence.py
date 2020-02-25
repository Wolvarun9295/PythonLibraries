sampleString = "restart"
char = sampleString[0]
sampleString = sampleString.replace(char, '$')
sampleString = char + sampleString[1:]
print(sampleString)
