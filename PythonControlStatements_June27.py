#5. Dictionary - key:Value ,Ordered,Mutable,not allowed duplicates
from operator import index

student = {
    'ID': 2,
    'name':'praneeth',
    'age':25,
    'score':200
}

print(student)
print(type(student))

'''
........................................
#Methods
........................................
'''

#Setdefault() - to add a default keypair

student.setdefault('school','high school')
print(student)


#1. ADD - adding a key pair

student['class']=10
print(student)

#2. Update - to add multiple keys

student.update({'section':'b','school':'HighSchool'})
print(student)

#3.get/access dict values:

print(student['class'])
print(student.get('name'))
print(student.items())

#4.Pop()

dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}
value = dict1.pop('c')
print(value)
print(dict1)


print('-----------------------------------------')
#5. popitem() - it removes last inserted key-value

dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}
value = dict1.popitem()
print(value)
print(dict1)


print('--------------------------------------------')
#6. Clear() - it delete all the data in dict

dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}
dict1.clear()
print(dict1)
print(type(dict1))


print('-----------------------------------------------------------------')

#Nested if - Using one if condition/statement inside another if condition/statement
'''
   if condition1"
       #code
       if condition2:
           code
           ...............

'''
from turtledemo.penrose import start

age = int(input("Enter your age :"))

if age >= 18:
    if age <= 60:
        print("You are eligible to apply")
    elif age >= 60:
        print("You are not eligible to apply, your age is exceeded")
else:
    print("You are not eligible to apply, Age must be between 18 and 60")


marks = int(input("Enter your marks :"))

if marks >= 40:
    print('Pass')
    if marks >= 90:
        print('Grade is A+')
    elif marks >= 80:
        print('Grade is A')
    elif marks >= 70:
        print('Grade is B')
    elif marks >= 60:
        print('Grade is C')
else:
    print('Fail')


# Iteration statements - while,for
'''
# 1. While loop

While loop is used when we need to repeat code as long as a condition is true.
if the condition is true then the code will repeat

Syntax :
       while condition :
             #Code Block

'''

print('------------------------------------')
#printing 1 to 10 numbers

i = 1
while i <= 10:
    print(i)
    i = i + 1


print('------------------------------------')
#printing even numbers

i = 2
while i <= 30:
    print(i)
    i+=2


print('------------------------------------')
#infite loop with break

i = 1
while True:
    print(i)
    if i == 5:
        break
    i = i + 1

print('------------------------------------')

# 2. for loop - used to repeat a block of code for each item in a sequence

'''
syntax :
       for variable in sequence:
                    #code Block
'''

for i in range(1,10):
    print(i)

print('------------------------------------')

for char in 'praneeth':
    print(char)

print('------------------------------------')
#printing sum for 1 to 10

total = 0
for i in range(1,11):
    total = total + i
print('sum',total)



print('------------------------------------')
#2. Transfer statement - break,continue,pass
#Break - using break to stop the loop

for i in range(1,11):
    if i == 5:
        break
    print(i)

print('------------------------------------')
#Contiue - using continue to skip the condition and continue to next one

for i in range(1,6):
    if i == 2:
        continue
    print(i)

#Pass
for i in range(1,11):
    if i == 5:
        pass
    print(i)

#else in for loop

for i in range(5):
    print('loop',i)
else:
    print('loop is finished')

print('------------------------------------')


#3. Conditional Statements - if,elif,else,nested if

#1. if statement

age = int(input("Enter your age :"))
if age >= 18:
    print('You are eligible to apply')


print('------------------------------------')
#2. else statement

age = int(input("Enter your age :"))
if age >= 18:
    print('You are eligible to apply')
else:
    print('You are not eligible to apply')

print('------------------------------------')

num = int(input("Enter your num :"))
if num % 2 == 0:
    print('Even')
else:
    print('Odd')

print('------------------------------------')

#3. elif statement

age = 33

if age < 10:
    print('child')
elif age < 18:
    print('Teenager')
elif age < 60:
    print('Adult man')
else:
    print('Senior Citizen')


print('------------------------------------')

#4. Nested if

marks = 60

if marks >= 40:
    print('Pass')
    if marks >= 90:
        print('Grade is A+')
    elif marks >= 80:
        print('Grade is A')
    elif marks >= 70:
        print('Grade is B')
    elif marks >= 60:
        print('Grade is C')
else:
    print('Fail')


# 5. Match case - to compare value against multiple patterns like(Switch case)

command = 'start'

match command:
    case 'start':
        print('System Starting............')
    case 'stop':
        print('System Stopped............')
    case _:
        print('Unknown command')


#6. Ternary operator - it is online code of if-else statement

#to find num is even or odd

num =10
result = 'Even' if num % 2 == 0 else 'Odd'
print('num is',result)


