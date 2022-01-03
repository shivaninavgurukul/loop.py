# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
#   print(word[char], end="")
# print("\n")

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],{"class":'V', "section":'A'}]
# for item in datalist:
#    print ("Type of ",item, " is ", type(item))
   

# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')
# print("\n")
	
# for fizzbuzz in range(51):
#     if fizzbuzz%3==0 or fizzbuzz%5==0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz%3==0:
#         print("fizz") 
#         continue
#     elif fizzbuzz%5==0:
#         print("buzz")
#         continue
#     print(fizzbuzz)

"row or colum"
# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col

# print(multi_list)


"count element and number"
# s = input("Input a string:-")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
# print("Letters", l)
# print("Digits", d)


"strong password"
# password=input("enter the letter and number and special symbol:-")
# if password>='letter' and "number" and "other symbol":
#     print("strong password")
# else:
#     print("not strong password")    


# iterow=15    
# for i in range(100, 500):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
#         items.append(s)
# print( ",".join(items))



"pattern S"
# row=15    
# col=18  
# result_str=""    
# for i in range(1,row+1):    
#     if((i<=3)or(i>=7 and i<=9)or(i>=13 and i<=15)):    
#         for j in range(1,col):    
#             result_str=result_str+"*"    
#         result_str=result_str+"\n"    
#     elif(i>=4 and i<=6):    
#         for j in range(1,5):    
#             result_str=result_str+"*"    
#         result_str=result_str+"\n"    
#     else:    
#         for j in range(1,14):    
#             result_str=result_str+" "    
#         for j in range(1,5):    
#             result_str=result_str+"*"    
#         result_str=result_str+"\n"    
# print(result_str);

"pattern A"
# for i in range(0,10):
#     if (i==0) or (i==5):
#         print(" * "*5)
#     else:
#         print("*            *")


"pattern E"
# for i in range(0,10):
#     if i==5 or i==5:
#         print( "* "*3)
#     else:
#         print("*    *")  


"month of code"
# print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
# month_name = input("Input the name of Month: ")
# if month_name == "February":
# 	print("No. of days: 28/29 days")
# elif month_name in ("April", "June", "September", "November"):
# 	print("No. of days: 30 days")
# elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
# 	print("No. of days: 31 day")
# else:
# 	print("Wrong month name") 


"sum digit"
# a=int(input("enter the number:-"))	
# b=int(input("enter the number:-"))
# if a+b>=15 and a+b<=20:
#     print("sum num",a+b)
# else:
#     print("not sum ")    

"Write a Python program to check a string represent an integer or not?"
# text = input("Input a string: ")
# text = text.strip()
# if len(text) < 1:
#     print("Input a valid text")
# else:
#     if all(text[i] in "0123456789" for i in range(len(text))):
#         print("The string is an integer.")
#     elif (text[0] in "+-") and \
#          all(text[i] in "0123456789" for i in range(1,len(text))):
#          print("The string is an integer.")
#     else:
#         print("The string is not an integer.") 

"tringle type"
# print("Input lengths of the triangle sides: ")
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

# if x == y == z:
# 	print("Equilateral triangle")
# elif x==y or y==z or z==x:
# 	print("isosceles triangle")
# else:
# 	print("Scalene triangle")

"month season"
# month = input("Input the month:- ")
# day = int(input("Input the day:- "))
# if month in ('January', 'February', 'March'):
# 	season = 'winter'
# elif month in ('April', 'May', 'June'):
# 	season = 'spring'
# elif month in ('July', 'August', 'September'):
# 	season = 'summer'
# else:
# 	season = 'autumn'
# if (month == 'March') and (day > 19):
# 	season = 'spring'
# elif (month == 'June') and (day > 20):
# 	season = 'summer'
# elif (month == 'September') and (day > 21):
# 	season = 'autumn'
# elif (month == 'December') and (day > 20):
# 	season = 'winter'

# print("Season is",season)

"midium number"
# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# c = float(input("Input third number: "))
# if a > b:
#     if a < c:
#         median = a
#     elif b > c:
#         median = b
#     else:
#         median = c
# else:
#     if a > c:
#         median = a
#     elif b < c:
#         median = b
#     else:
#         median = c
# print("The median is", median)

"year month day"
# year = int(input("Input a year: "))
# month = int(input("Input a month [1-12]: "))
# day = int(input("Input a day [1-31]: "))
# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False
# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30
# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

"table in for loop me"
# n = int(input("Input a number: "))
# for i in range(1,11):
#    print(n,'x',i,'=',n*i
   



