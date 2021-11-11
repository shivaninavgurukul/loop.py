# k = 0
# num1 =int(input("enter any number"))
# if num1==0 or num1==1:
#     k =1
# for i in range(2,num1) :
#     if num1%i==0:
#         k=1
# if k==1:
#     print("prime number")
# else:
#     print("not prime")  
# 

num = int(input("enter the number :"))
count = 0
i =1
while (i<=num):
    if(num%i==0):
         count = count+1
    i = i+1
if(count==2): 
    print("prime number")
else:
    print("not prime number")

    



