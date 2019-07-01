#Write a program to check whether given input is palindrome or not
str1 =input("Enter a string: ")
str2 = str1.lower()
rev_str = reversed(str1)
if list(str1) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")