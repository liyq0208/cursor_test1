l1 = [100, 1000, 10, 400, 25, 40, 0]
l2=l1
l2.sort()
print("l1   l2")
for i in range(len(l1)):
    print(f"{l1[i]:<5}{l2[i]:<5}")
print("--------------------------------")
l1 = [100, 1000, 10, 400, 25, 40, 0]
l2=l1.copy()
l2.sort()
print("l1   l2")
for i in range(len(l1)):
    print(f"{l1[i]:<5}{l2[i]:<5}")
