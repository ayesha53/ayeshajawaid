a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
op=input("Enter operator + , - , * , / : ")
if op=="+":
    
    def add(num1,num2):
        my_sum=num1+num2
        print(my_sum)
    add(a,b)
elif op=="-":

    def sub(num1,num2):
        my_sub=num1-num2
        print(my_sub)
    sub(a,b)
elif op=="*":
        
        def mul(num1,num2):
            my_mul=num1*num2
            print(my_mul)
        mul(a,b)
elif op=="/":
            
            def div(num1,num2):
                my_div=num1/num2
                print(my_div)
            div(a,b)
else:
                print("you entered wrong operator")