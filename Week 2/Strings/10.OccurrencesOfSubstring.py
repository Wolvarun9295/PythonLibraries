inputString = input('Enter something: ')
countThis = input('Enter the substring you want to find occurrences of: ')
newString = inputString.count(countThis)
print(f'The substring {countThis} occurs {newString} times in the String')
