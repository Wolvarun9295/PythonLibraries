# Initializing a dictionary.
sampleDictionary = {0: 10, 1: 20}
# Taking input from user for key:value pair to be added.
key = int(input('Enter the key: '))
value = int(input('Enter the value: '))
# Updating the dictionary.
sampleDictionary.update({key: value})
print(f'The updated dictionary is: {sampleDictionary}')
