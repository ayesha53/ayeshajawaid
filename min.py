import random
lst1 = []
for i in range (0,5):
    lst1.append(random.randint(30,60))
print(lst1)
min_val=lst1[0]
min_idx=0
for i in range(1,len(lst1)):
    if min_val > lst1[i]:
        min_val = lst1[i]
        min_idx = i
print("The minimum value is: " ,min_val)
print("The index of minimum value is " ,min_idx)
