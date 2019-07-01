#13.	Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
if (a+b) == 5:
    print("True")
elif (a==b):
    print("True")
elif (a-b) ==5:
    print("True")
else:
    print("False")