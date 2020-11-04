# let's create a greeting function

# syntax: def name_of_function():
# each funtion has a block of code tto execute to ideally run one task

# def greeting(name):
#     print("welcome on board " + name)
#
# # if we execute this program now it would display nothing as we have not called this function
#
# # syntax: to call function
#
# greeting("Daniel")
# calling our greeting function
# this will execute the code inside the function

# create a new function that takes 2 arguments as ints and adds the value of the two arguments

def add(num1, num2):
# creating an add function that takes 2 arguments
    print(num1 + num2)
# Display the sum of the arguments received

add(4, 5)
#
#num1 and num2 can be declared twice as they are part of two diff functions so do not appear as duplicates

def subtract(num1, num2):
# creating a function to subtract two arguments
    print(num1 - num2)

# calling function and passing two values

subtract(5, 2)

#######

def subtract(num1, num2):
# creating a function to subtract two arguments
    return num1 - num2

subtracted_value = subtract(10,2)
# calling function and passing two values

print(subtracted_value)


# create a function to *
def multiply(num1, num2):
    return num1 * num2


print(multiply(10, 5))

# call function


# return
#     return 10, 5

# create a function to /
def divide(num1, num2):
    return num1 / num2

print(divide(10, 5))


def mod(num1, num2):
# we use a return statement which is key to
    return num1 % num2

    print(mod(10, 5 ))
# create a function to %





