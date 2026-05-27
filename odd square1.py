l1 = [1, 2, 3, 4, 5]
l2 = []
for i in l1:
    if i % 2 == 1:
        l2.append(i ** 2)
    else:
        print("No odd number")

print(l2)