import random

#Addition
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)
print('What is ', num1, '+', num2, '?')
ans1 = eval(input("Your answer: "))
add = num1 + num2
print(num1, '+', num2, '=', add)
if ans1 == add:
    print('Your answer is correct!')
    print("-----------------------")
else:
    print('Your answer is incorrect!')
    print("-----------------------")

#Subtraction
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)
print('What is ', num1, '-', num2, '?')
ans2 = eval(input("Your answer: "))
sub = num1 - num2
print(num1, '-', num2, '=', sub)
if ans2 == sub:
    print('Your answer is correct!')
    print("-----------------------")
else:
    print('Your answer is incorrect!')
    print("-----------------------")

#Multipication
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)
print('What is ', num1, '*', num2, '?')
ans3 = eval(input("Your answer: "))
multi = num1 * num2
print(num1, '*', num2, '=', multi)
if ans3 == multi:
    print('Your answer is correct!')
    print("-----------------------")
else:
    print('Your answer is incorrect!')
    print("-----------------------")

#Division
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)
print('What is ', num1, '/', num2, '?')
ans4 = eval(input("Your answer: "))
div = num1 / num2
rounded = round(div, 2)
print(num1, '/', num2, '=', rounded)
if ans4 == rounded:
    print('Your answer is correct!')
    print("-----------------------")
else:
    print('Your answer is incorrect!')
    print("-----------------------")
