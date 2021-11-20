# n = int(input("enter the number of rows:-"))
# for i in range(n):
#     print((chr(65+i)+ " ")*(i+1))


user = int(input("enter the number"))
a = user//10
b = user//1000%10
if b==4:
    print("yes")
else:
    print ("no") 
