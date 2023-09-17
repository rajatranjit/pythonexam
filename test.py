
#for i in range(1000):
#    print("Happy Dashain")

    
#print("Happy Dashain \n"*100)

#age= input("what is your age: \n")
#print("your age is",age)

#age = (input("Enter your age:"))
#print ("your age is :",type(age))

#age = int(input("ENter your age:"))
#print ("your age is :", type(age))

#u_age = int(input("enter your age: \n"))
#pyear = int(input("Enter your year: \n"))
#birth_y = pyear - u_age
#print("Birth Year",birth_y)


#check a number is if greater than or lesser than 100

#user_input = int(input("Enter a numer:"))
#if user_input > 100:
 #   print("Number is greater than 100")
#elif user_input == 100:
 #   print("Number is equal to 100")    
#else:
#    print("number is less than 100")


#wap to count number of even numbers between 1 and user provided value

#user_value = int(input("Enter an upper limit: "))
#even_count = 0
#for number in range(1, user_value+1):
#    if number % 2 == 0:
#        even_count += 1
#
#print("The number of even number is:", even_count)

# check number for even or odd
#num=int(input("write the number to check even or odd"))
#if num%2 == 0:
#    print("Number is Even")
#else:
#    print("Number is odd") 


# 
#for i in range (0,1,10):
#    print(i)

#### find percentage of five numbers ###
# marks = []
# for i in range(0,5):
#     marks=float(input("enter the marks of five subjects:\n")):

# total_mark=sum(marks)
# percentage=(total_mark/500)*100
# print(percentage)

# total=0
# print(type(total))
# for i in range(0,5):
#     num=int(input("enter the number:"))
#     total=total+num
# print((total/500)*100)
    

# for i in (0,5):
#     print(i)

# for i in ("ram","shyam","hari"):
#     print(i)

# for i in range(0,10,2):
#     print(i)

## 13 multiplication table ##

# for i in range (1,11):
#     print(i*13)

# for i in range(1,11):
#     print(f"13*{i}=",13*i)
    

# name='rdp'
# age=3389
# print(f"hello my name is {name} i am {age} years old")
# print("hello my name is {} i am {}years old".format(name,age))
# print("hello my name is",name,"i am",age,"years old")

# create a chatbot #

# name= input("ENter your name \n")
# print(f"Hello {name} I am a chatbot")
# age=int(input("Enter your age \n"))
# print(f"you are {age} years old and i am 1 day old")
# add=input("enter your address \n")
# print(f"You live in {add} and I live in a computer")

# user_value=int(input(" enter a number for which you want me to write a multiplication \n"))
# print(f"The multiplicatin table of {user_value} is given below:")
# for i in range (1,11):
#     print(f"{i}*{user_value}=",i*user_value)
    
# print("You are welcome")

#WAP to count numbers of prime number between 1 and user provided number 

# num=int(input("Enter a number: "))
# count=0
# sum=0
# for num in range(1,num+1):
#     if num>1:
#         for i in range(2, int(num**0.5) +1):
#             if (num % i) ==0:
#                 print(f"{num} is not prime number")
#                 break
#         else:
#             count=count+1
#             print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")
# print(count)


# find sum of first 65 prime numbers

# num=0
# count=0
# sum=0
# while count < 65:
#     num=num+1
#     if num >1:
#         for i in range(2, int(num**0.5) +1):
#             if (num % i) ==0:
#                 break
#         else:
#             sum=sum+num
#             count=count+1
#             print(sum)



#WAP to calculate sum of first fifty odd number

# first=1
# i=1
# sum=1
# while i<50:
#     num=first+2
#     first=num
#     sum+=num
#     i+=1
# print(sum)



# WAP to find multliplication factor of any number provided by user

# user_num=int(input("Enter a number to find factorial: "))
# for num in range(1,user_num+1):
#     if (user_num%num)==0:
#         print(num)
    


# to find the factorial of any number

# num=int(input("Enter a num to find factorial: "))
# fact=1
# if num <0:
#     print(f"{num} is negative and doesnot have any factorials")
# elif num ==0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num+1):
#         fact=fact*i
#     print(f"the factorial of {num} is {fact}")

#to show the division of percentage obtained by students
#to find a perfect cube root




# to show different formatting styles in python
#can you use switch case in python
#wap to check if a given number is palindrome or not

# num=int(input("Enter the number to check for palindrome: "))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")









#wap to take a string and check if the string is ram

# string= input("Enter a string ")
# if string== 'ram':
#     print("string is ram")
# else:
#     print("string is not ram")








# num=30
# count=0
# for num in range(1,num+1):
#     if num>1:
#         for i in range(2, int(num**0.5) +1):
#             if (num % i) ==0:
#                 break
#         else:
#             print(f"{num} is a prime number")
#             print(num*num)


# square of first 10 prime numebers

# num=int(input("Enter a number: "))
# num=0
# count=0
# # sum=0
# #for num in range(1, num+1):
# while count <10:
#     num=num+1
#     if num >1:
#         for i in range (2, int(num**0.5)+1):
#             if (num % i) ==0:
#                 print(f"{num} is not a prime number")
#                 break
#         else:
#             count=count+1
#             print(f"{count} {num} is a prime number and square is {num*num}")
#     else:
#         print(f"{num} is not a prime number")
# print(count)

# check number for prime

prime=int(input("Enter the number to check: "))
if prime>1:
    for i in range(2,int(prime*0.5)+1):
        if (prime%i==0):
            print(f"{prime} is not prime number")
            break
    else:
        print(f"{prime} is prime number")
else:
    print(f"{prime} is not prime number")

