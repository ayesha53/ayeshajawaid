first_number=int(input("Enter number "))
second_number=int(input("Enter number "))
operator=input("Enter operator")
if operator=="+":
    print(int(first_number)+int(second_number))
elif operator=="-":
    print(int(first_number)-int(second_number))
elif operator=="*":
    print(int(first_number)*int(second_number))
elif operator=="/":
    print(int(first_number)/int(second_number))
else:
    print("You enterd wrong operator")




