set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

difference1 = set1 - set2
difference2 = set2 - set1

union = set1 | set2

symmetric_difference1 = set1 ^ set2
symmetric_difference2 = set2 ^ set1

intersection1 = set1 & set2
intersection2 = set2 & set1

print("Set Difference")
print("set1 - set2 : ", difference1)
print("set2 - set1 : ", difference2)
print("\nUnion of Sets")
print("set1 | set2 : ", union)
print("\nSymmetric Difference")
print("set1 ^ set2 : ", symmetric_difference1)
print("set2 ^ set1 : ", symmetric_difference2)
print("\nSet Intersection")
print("set1 & set2 : ", intersection1)
print("set2 & set1 : ", intersection2)
