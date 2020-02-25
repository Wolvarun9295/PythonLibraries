sampleDict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
              {"VIII": "S007"}]
print(sampleDict)
uniques = set(value for dictionary in sampleDict for value in dictionary.values())
print(uniques)
