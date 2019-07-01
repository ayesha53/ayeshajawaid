#Write a Python program that accepts a string and calculate the number of digits and letters
def letter_count(str): 
	count = 0
	letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") 
	for alphabet in str: 
		if alphabet in letters: 
			count = count + 1
	print("No. of letters :", count) 
def num_count(str): 
	count1 = 0
	numbers= set("1234567890") 
	for nums in str: 
		if nums in numbers: 
			count1 = count1+ 1
	print("No. of digits :", count1) 
str = input("Enter string to check: ")
letter_count(str) 
num_count(str)