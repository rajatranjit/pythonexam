#WAP to find square of every element of list and sum of squares





# list = [2,4,3,5,7]
# sq_list=[]
# sum=0
# for num in list:
#     sq=num*num
#     sq_list.append(sq)
#     sum +=sq
# print(list)
# print(sq_list)
# print(sum)

#WAP to check if a given string is present in list or not

# list=[1,3,6,8,'ram','hari']

# string=input("Enter a string to check: ")
# for string in list:
#     # if list(i)==string:
#         print(f"{string} is found in list")
# else:
#         print(f"{string} is not found in the list")


# wap to copy list elements into another list 

# list1=[2,4,5,3,6]
# list2=tuple(list1)
# list1.append(12)
# print(list1)
# print(list2)




#wap to take input as combination of character abc in any order given that the value of a is 20 be is 18 and c is 22
# now find the total weight for the combination of character


# a=input("Enter characters:")
# print((a.count("A")*20)+(a.count("B")*18)+(a.count("C")*22))

# dict_val={"A":20,"B":18,"C":22}
# a=input("Enter characters:")
# print((a.count("A")*dict_val["A"])+(a.count("B")*dict_val["B"])+(a.count("A")*dict_val["C"]))

# import ramdom
# for i in range(100):
#     rnum=random.randint(1,48)
#     print(rnum)



# dict_val={"A":20,"B":18,"C":22}
# print(type(dict_val))
# for key,value in dict_val.items():
#     print(key)
#     print(value)

    
    
# lst=[1,2,3,4,5]
# print(type(lst))
# for i in lst:
#     print(i)

# def function_name():
#     print("I am inside function")

# function_name()


# def function_name(arg1,arg2,arg3):
#     print("I am inside function")
#     print(f"{arg1} {arg2} years old and earns {arg3}")

# function_name("ram", 20, 100000)
# # function_name()
# print("hello")


#Function with return type 
# def square(num):
#     sq = num*num
#     return sq

# squared_value = square(5)
# print("square is ", squared_value)


#function without arguement
# def square():
#     num=int(input("Enter a number "))
#     sq=num*num
#     return sq

# squared_value = square()
# print("square is ", squared_value)

# def square():
#     print("function")
# square()


#function with default arguemnt
# def square(num=5):
#     sq=num*num
#     return sq

# squared_value = square(6)
# print("square is ", squared_value)



# def square(num,num2=2):
#     sq=num*num*num2
#     return sq

# squared_value = square(1,2)
# print("square is ", squared_value)



# def square(num,num2=4):
#     sq=num*num*num2
#     return sq

# squared_value = square(1,5)
# print("square is ", squared_value)


# def check(num):
#     if num==5:
#         return True
#     if(check(5)):
#         print("Given argument is 5")
#     else:
#         print("not 5")


# def check(num):
#     print("inside")
#     if num==5:
#         return True
# if(check(6)):
#         print("Given argument is 5")
# else:
#         print("not 5")


# def check(num):
#     print(f"{num*num}")
# check(5)
# check(6)
# check(7)        


# def check(num):
#     return num
#     print(f"{num*num}")
# a=check(5)
# print("function after 1st called")
# a=check(6)
# a=print("function after 2nd is called")
# check(7)        


# def check(num):
#     if num<5:
#         return num
#     return num*num

# a=check(4)
# print(a)
# b=check(6)
# print(b)      

# num = 5   # this is outside function and is global variable
# def number(num)
#     num=6
#     print(num)
# number(7)
# print(num)



# wap to find simple interest

# def si_interest(p,t,r):
#     interest=(p*t*r)/100
#     return interest

# simple_interest= si_interest(25000,5,10)
# print("the simple interest is ", simple_interest)

# wap to check if a given number is prime or not

# def prime(num):
#     if num>1:
#         for i in range(2,int(num*0.5)+1):
#             if (num%i)==0:
#              print(f"{num} is not a prime number")
#              break
#         else:
#             print(f"{num} is a prime number")

# prime_num=prime(19)


# wap weighted sum of character

# def sum_character(a):
#     a=input("Enter characters")
#     print((a.count("A")*20)+(a.count("B")*18)+(a.count("C")*22))

# total_weight=sum_character("")

# wap to define 5 user defined functions in same program


# def addition(num1,num2):
#     sum=num1+num2
#     return sum

# add= addition(6,7)
# print("sum of numbers is ",add)

# def subtraction(num1,num2):
#     dif = num1 - num2
#     return dif

# sub= subtraction(9,3)
# print("difference of numbers is ",sub)

# def multiplication (num1,num2):
#     mul=num1*num2
#     return mul

# times= multiplication(7,9)
# print("multliplication of numbers is ",times)

# def division(num1, num2):
#     div = num1/num2
#     return div

# divide= division(10,5)
# print("division of numbers is ",divide)

# def square(num)
#     sq=num*num
#     return sq

# squared= square(7)
# print("square of number is ",squared)

# wap to show use case for different types of functions




# wap to count number of squares numbers between 50 and 929

# count=0
# for numb in range (50, 930):
#      for num in range(1,100):
#         if(int(num*0.5)**2)==numb:
#             count+= 1
# print(f"the number of squares between 50 and 929 is:{count}")

# wap to sum the digits provided by the users


# def sum(user_num):
#     sum=0
#     for digit in str(user_num):
#         sum+=int(digit)
#     return sum

# num_sum=sum(2345)   
# print(num_sum)



# wap to calculate mody mass index

# def bodyMass_Index(height, weight):
#     BMI= weight/(height*height)
#     return BMI
# BM_Index= bodyMass_Index(2,50)
# print("The body mass index is ",BM_Index)


# functions has arguements
# before call function should be defined
# if body has return program exits from function
# arguments can be int string, bool, float
# no argument return
#  argument return
# no arguemt no return
#  argument no return
#  default arguemtn

# convert 3 year 12 month 4 days 21 hours, 52 min and 20 sec to seconds


# def year(year1):
#     sec1=year1*12*30*24*60*60
#     return sec1
# year_sec=year(3)
# print(year_sec)

# def month(month1):
#     sec2=month1*30*24*60*60
#     return sec2
# month_sec=month(12)
# print(month_sec)

# def days(days1):
#     sec3= days*24*60*60
#     return sec3
# days_sec=days(4)
# print(days_sec)

# def hours(hour1):
#     sec4=hour1*60*60
#     return sec4
# hours_sec=hours(21)
# print(hours_sec)

# def min(min1):
#     sec5=min1*60
#     return sec5
# min_sec=min(52)
# print(min_sec)

# sec6=20
# print(year_sec+month_sec+days_sec+hours_sec+min_sec+sec6)


# convert82930000 minutes into year month day hour and minutes


# generate fibonacci series upto user given number

# count=int(input("Enter a number upto which you want fibonacci series: "))
# i=0
# j=1
# count1=0
# if count==1:
#     print(i)
# elif count>1:
#     while count1<count:
#         num=i+j
#         print(i)
#         i=j
#         j=num
#         count1+=1

#factorial of number

n=int(input("ENter a number to find factorial: "))
fact=1
for num in range (1,n+1):
    fact*=num
    
print(fact)




