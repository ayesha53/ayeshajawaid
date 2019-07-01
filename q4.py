#Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)
num = int(input("Enter a number: "))
result=str(num+(num*num)+(num*num*num))
print("The result of given number is: " +result)