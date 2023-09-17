#  10. Write a Python program that does the following:
# Defines three functions: calculate_rectangle_area(), calculate_circle_area(), and
# calculate_triangle_area(), each of which takes the necessary parameters and returns the area of the
# respective shape.
# Prompt the user to choose a shape (rectangle, circle, or triangle).

# import math

# def calculate_rectangle_area(length,breadth):
#     rec_area=length*breadth
#     print(f"The area of rectangle is {rec_area} meter square")
#     return

# def calculate_circle_area(radius):
#     cir_area=(radius*radius)*3.14
#     print(f"The area of circle is {cir_area} meter square")
#     return

# def calculate_triangle_area(base,height):
#     tri_area=0.5*base*height
#     print(f"The area of Triangle is {tri_area} meter square")
#     return


# shape1=(input("please choose the shape: (rectangle, circle, triangle): "))

# if shape1==  'rectangle':
#     length =int (input("Please enter length: "))
#     breadth=int (input("ENter the breadth of rectangle: "))
#     rect_area=calculate_rectangle_area(length,breadth)
#     print(rect_area)

# elif shape1== 'circle':
#     radius = int (input("Please enter the radius of circle: "))
#     circ_area=calculate_circle_area(radius)
#     print(circ_area)

# elif shape1 == 'triangle':
#     base= int (input("Enter base of triangle: "))
#     height=int(input("Enter height of the triangle: "))
#     tria_area=calculate_triangle_area(base,height)
#     print(tria_area)

# else:
#     print("invalid input")


#. Check whether a given number is perfect cube or not.

# num=int(input("Enter a number to check for perfect cube: "))
# if int(num**(1/3))**3==num:
#     print(f"{num} is perfect cube number")
# else:
#     print(f"{num} is not perfect cube")


# Given a=20A, A=20b, b=16C, C=29d, d=33. For “aabACdCA” find the numerical value.

# d=33
# C=29*d
# b=16*C
# A=20*b
# a=20*A

# input="aabACdCA"
# print((input.count('a')*a) + (input.count('b')*b) + (input.count('A')*A) + (input.count('C')*C) + (input.count('d')*d))




#For a list [3,4,5,6,7] create nested list to show multiplication table of every element up-to 10.output format- [[3,6,9,…..30],………..]

# list=[3,4,5,6,7]
# mul=[ ]
# for num in list:
#     mul1=[]
#     for i in range(1,11):
#         new=num*i
#         mul1.append(new)
#     mul.append(mul1)
# print(mul)


#Given a tuple (44,4,5,6,7) manipulate this tuple to find square of every element and replace the tuple with squared value.

# my_tuple=(44,4,5,6,7)
# list=list(my_tuple)
# list1=[ ]
# for num in list:
#     new=num*num
#     list1.append(new)
   
# new_tuple=tuple(list1)
# print(new_tuple)

#  Can there be two keys with same name. Justify with program.
#no there cannot be two keys with same name
# my_dict={
#     "name" :"ashok",
#     "name" : "nabin"
# }
# print(my_dict)

#5. From two list find the minimum and maximum value.

# list1=[1,2,3,47,8]
# list2=[99,45,36,77,98]

# print(min(list1))
# print(max(list2))


# Take input from user in the form of string both in upper and lowercase. Now separate upper and lowercase characters.

# user_inp=input("Enter characters: ")
# upper=' '
# lower=' '
# for char in user_inp:
#     if char.isupper():
#         upper+=char
#     else:
#         lower+=char
# print(upper)
# print(lower)


#Given a list [1,2,3,4,5,6,7] randomly choose element from this list and create a new list of length 7. There shouldn’t be any repetitive element.(Don’t use random.shuffle())

# import random
# list=[1,2,3,4,5,6,7]
# list1=random.sample(list,7)
# print(list1)

#  Convert 122430120 minutes into years months days hours and minutes.

# min=122430120

# year=int((((min/60)/24)/30)/12)
# print(year)

# year1=year*12*30*24*60
# min2=min-year1

# month=int(((min2/60)/24)/30)
# print(month)

# month1=month*30*24*60
# min3=min2-month1

# day=int((min3/60)/24)
# print(day)

# day1=day*24*60
# min4=min3-day1

# hour=int(min4/60)
# print(hour)

# hour1=min4=day1

# print(hour1)



#challenge lab#

list=[ ]
count=0
for num in range(2,251):
    for i in range(2,int(num*0.5)+1):
        if (num%i)==0:
            break
    else:
        cunt=count+1
        list.append(num)
print(list)

with open('output.txt', 'w') as f:
    print(list, file=f)




