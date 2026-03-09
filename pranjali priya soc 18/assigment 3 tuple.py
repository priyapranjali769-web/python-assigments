#To program the operations on tuple
#Creating a tuple of even numbers
tup_1 = (2,4,6,8)                             
print("Your first tuple is:",tup_1)

#To access the elements of the tuple
print("First element of the tuple is:",tup_1[0])
print("Last element of the tuple is:",tup_1[-1])

tup_2 = (1,3,5,7)                             #Creating tuple 2
print("Your second tuple is:",tup_2)

#Creating nested tuple
nested_tup =((2,4,6,8),(1,3,5,7))                       
print("Your nested tuple is:",nested_tup)                 #Nested tuple

#Concatinating tuple 1 and tuple 2
concatinated_tup = tup_1 + tup_2
print("Your concatinated tuple is:",concatinated_tup)     #Concatinated tuple

new_tup = tup_1 + (10,12,14)
print("New tuple is:",new_tup)                  #Adding new elements in the tuple

#Repeating tuple
repeated_tuple = tup_2*2
print(repeated_tuple)             