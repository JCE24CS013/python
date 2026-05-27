l1 = [1,2,3,2,5,3,7,1]
def duplicate(l1):
    duplicates = set()
    for i in l1:
        if l1.count(i) > 1:
            duplicates.add(i)
    return duplicates
print(duplicate(l1))