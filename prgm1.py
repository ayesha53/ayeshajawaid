print("****MARKSHEET****")
Student_name=input("Enter your name: ")
English=int(input("Enter your marks in English: "))
Chemistry=int(input("Enter your marks in Chemistry: "))
Pak_Studies=int(input("Enter your marks in Pak_Studies: "))
Sindhi=int(input("Enter your marks in Sindhi: "))
Comp_Sci=int(input("Enter your marks in Computer Science: "))
total=English+Chemistry+Pak_Studies+Sindhi+Comp_Sci
print(total)
avg=(total/5)
if avg>=80:
    print("Grade A1")
elif avg>=70:
    print("Grade A")
elif avg>=60:
    print("Grade B")
elif avg>=50:
    print("Grade C")
else:
    print("You are fail")
    











