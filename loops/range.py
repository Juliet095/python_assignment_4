# Range function

def total_marks():
    marks = [60,70,80]
    sum = 0
    for mark in marks:
        sum+=mark
    print(sum)
total_marks()

name = "Birungi"
for item in name:
    print(item)

marks = [60,70,80]
for mark in marks:
    print(mark)


def total_marks():
    marks = [60,70,80]
    sum = 0
    for mark in marks:
        sum+=mark
    print(f"the total marks is: {sum}")
total_marks()


#syntax
# Range ( start, stop , step)
#Basic example
# using a loop print all numbers from 0 to 6

for num in range (7):
   print(num)


# 0 to 10
for num in range (11):
   print(num)


#1 to 20
for num in range ( 1,21):
    print(num)

# 1 to 20
def one_to_twenty():
    for num in range (1,21):
        print(num)
one_to_twenty()

# print the following range of even numbers( 2,4,6,8,10).

def even_numbers():
    for even in range(2,11,2):
     print(even)
even_numbers()

#print the following range of odd numbers(0,3,5,7,9)

#

# Lists $ Turples
# Similarities
# Both are mutable(can be changed)
#Both ordered
#Both indexed
#SYNTAX
#Lists[]
#Turples()

products = ['pen','pencil','book']
colors = ('red','green','pink')
#Add rubber to the products list
products.append ('Rubber')
print(products)
#Insert ruler at the second position
products.insert ( 1, "ruler") 
print(products)
#Display the len
print(len(products))

#Add purple to the turple
#Items can not be modified in a turple
#converting a turple into a list
colors =('red','green','pink')
new_colors =list(colors)
print(type(new_colors))
new_colors.append('purple')
print(new_colors)

fruit =('apple')
print(fruit,type(fruit))

#SETS
#They are immutable
#Unordered

#syntax for set {}
set_of_numbers = { 2, 3,5}

#Dictionaries
#key value pair
#access item(values)
#change items
#add items
#remove items 
#syntax
student = {'name':'Gillian', 'age':22 ,'location':'muyenga'}
print(student)
#accessing items in the dictionary
print(student['name'])
print(student['age'])
print(student['location'])
fruits = {1:'apple',2:'orange',3:'banana'}
print(fruits)

#print the keys of the student dictionary
student.keys()
print(student.keys())

#print the length of the dictionary
print(len(student))

#add a key contact to the student dictionary
student['contact'] = '0782456782'
print(student)

#changing 
#update the name Gillian to Apio
student['name'] = 'Apio'
print(student)

#access the values
print(student.values())

#Remove the contact key from the dictionary
del student['contact']
print(student)

student.pop('contact')


