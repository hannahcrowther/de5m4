hello_world = "HelloWorld"


print(hello_world[1:5])  #finding first 5 letters of hello_world (negatives will count from the end)

a = [] #empty list
b = [1, "string", True, 2.3] #list with different data types
print(b[-1]) #finding last item in list b 
print(b[-3:]) #finding last 3 items in the list - will be printed as a list. 

b.append("test") #adds test to list b
print(b)
b.insert(2, "myinsert") #inserts myinsert into position 2 of list b
print(b)

print(len(a)) #len shows hte list's lenght
print(len(b))

b[1:2] = ["replace1", 2] #replaces the list items at the specified list points - an empty list would delete the points. 
print(b) 

del(b[1]) #deletes the item in position 1 from the list
print(b)

#Multidimension List

c = [a, b] #combines the two lists made above 
print(c)

#you can also append lists to themselves 

print(c[0]) # returns first list. replacing the 0 with a 1 would return the second list. 

print(c[1][1]) #returns the 2nd item from the 2nd list

#SETS

#Are immutable
#lists can have duplicates, sets cannot

a = set()
b = {1, "string", 2.3, 1, 1, 1, True} #both these will create a set - set b will remove the duplicates and adjust the order
                                      #The True will also disappear, because True becomes 1, which is already present
print(b)
                                
if "string" in b :  #checking if the item string is in b at a specific position (this doesn't actually work on sets)
    print("true")
else: print("false") 


#Dictionaries: Can build relationships between sets
#Are mutable
#Can return associated values when fed a value. For example, a city to country dictionary, if I asked for New York, it would return New York, USA
# {} - creates dictionary, not set, hence needing the function set to create an empty set

b = {'a': 1, 'b': 2, 'c': 3 } #creates dictionary with related values. 

print(b['a']) #returns values associated with a

b['a'] = "anything" # changes the 1 associated with a to 'anything'

print(b['a'])

b[15] = 5 #adds another item to the dictionary b. 

print(b)
