#Write a Python program to convert an integer to Binary, Octal and Hexadecimal numbers 
dec = int(input("Enter decimal number: "))
print("The decimal value of",dec,"is: ")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")