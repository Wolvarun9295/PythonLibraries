inputString = input('Enter something: ')
sort = [word for word in inputString.split(",")]
print(",".join(sorted(list(set(sort)))))
