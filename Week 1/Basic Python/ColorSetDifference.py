# Declaring two sets.
colorList1 = {"White", "Black", "Red"}
colorList2 = {"Red", "Green"}
# Initializing an empty list.
difference = []
# Performing the Set Difference A not in B.
for i in colorList1:
    if i not in colorList2 and i not in difference:
        difference.append(i)
print(difference)
