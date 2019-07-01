#.Write a Python program to construct the following pattern, using a nested loop number. 
n=10
for i in range(n):
    for j in range(i):
        print ( i, end="")
    print('')