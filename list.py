employ_list=["Ayesha" , 21 , "Karachi"]
print("Employ name is " +employ_list[0]+ " Employ age is " +str(employ_list[1])+
       " Employ city is " +employ_list[2])
employ_list.append("Pakistan")
print(employ_list)
employ_list[2] = "Lahore"
print(employ_list)
employ_list.insert(1 , "Maria")
print(employ_list)
employ_list.pop()
print(employ_list)
del employ_list[1]
print(employ_list)
employ_list.pop(0)
print(employ_list)