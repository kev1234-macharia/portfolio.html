#adding all items of one list to another
prime_numbers =[2,3,5,7,9]
print ("list1:",prime_numbers)
even_numbers =[4,6,8,10,12]
print("list2:",even_numbers)
#join two lists
prime_numbers.extend(even_numbers)
print("list after append:",prime_numbers)