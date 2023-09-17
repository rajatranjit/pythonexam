# my_list=[1000,'potato','medicine',1.2,'tomato']
# print(my_list[1])
# print(my_list[-3])
# print(my_list[:3])

# my_list.append('masala')  # add masala at last list
# print(my_list)
# my_list.insert(3,'masala')  #insert masala at 4th position
# print(my_list)
# my_list[0]=500  # replace 1000 with 500
# print(my_list)

# my_list.remove(my_list[1])#remove potato from the list
# print(my_list)
# popped_value = my_list.pop(1) # stores removed item as pop
# print(popped_value)
# print(my_list)
# my_list.sort()
# print(my_list)

# my_list2 = [1,2,4,21,452,3,5]
# my_list2.sort()  #sorts lists in ascending order
# print(my_list2)
# my_list2.sort(reverse=True) #sorts lists in descending order
# print(my_list2)
# print(2 in my_list2)   # check for 2 in the list
# print(2 not in my_list2) # check for if 2 not in list
# print(22 in my_list2)
# # my_list2.clear()  cleares the list
# print(my_list2)

# my_list +=my_list2
# my_list = my_list +my_list2
# print(my_list)



#ListTasks
# numbers = [1,3,5,7,5,9]
# print(numbers)
# print(numbers[1])
# numbers[2]=10
# print(numbers)
# numbers.append(12)
# print(numbers)
# numbers.remove(numbers[4])
# print(numbers)
# sliced_list = numbers[1:4]
# print(sliced_list)
# combined_list = numbers + sliced_list
# print(combined_list)
# print(8 in combined_list)
# combined_list.sort()
# print(combined_list)

#--------Tuple--------#  can not be changed in the middle and  remains constant
# my_tuple = (1,2,4,2,3,4,)
#my_tuple[2] = 50    # this is error in tuple
# print(my_tuple)
# a,b,c,d = my_tuple    # this is called unpacking
# print(a)
# count_1 = my_tuple.count(4)
# print(count_1)

# my_tuple = (1,2,4,2,3,4)*10
# print(my_tuple)
# print(min(my_tuple))
# print(max(my_tuple))

# my_tuple = (1,2,4,2,3,4,'a','b') can be both numbers and strings
# my_tuple = (1,2,4,2,3,21,21,1)
# sr=sorted(my_tuple)
# print(sr)

# sr=sorted(my_tuple,reverse=True)
# print(sr)

#converting list to tuple
# my_list = [1,2,3,4,6]
# my_tuple = tuple(my_list)
# print(type(my_tuple))

#converting tuple to list
# my_list = (1,2,3,4,5)
# my_tuple = list(my_list)
# print(type(my_tuple))



#---------------TupleTask------------#


my_tuple =(10,20,'a','b',True)
c,d,e,f,g =my_tuple
print(e)

tuple1 =(1,2,3)
tuple2 =('x','y','z')

list1 = list(tuple1)
list2 = list(tuple2)
combined_list = list1 + list2
concatenated_tuple = tuple(combined_list)
print(concatenated_tuple)

repeated_tuple = my_tuple *10
print(repeated_tuple)

print(len(concatenated_tuple))

my_list = list(my_tuple)
print(my_list)
sliced_list = my_list[2:]
sliced_tuple = tuple(sliced_list)
print(sliced_tuple)
