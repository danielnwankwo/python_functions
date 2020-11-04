# this lesson covers python functions

## what are functions and what are they used for 
### how to create a function
### functions are best practices 

## DRY DON'T REPEAT YOURSELF

- how to create a function 

- Syntax: def name_of_function():

- what are functions 

# best practice 
- best practice is to have a small block of code in any function that does one job

- psuedo coding - one line of explanation 
- HINTs: create hints in simple bullet points or pointers 
- comments regarding your function results 

- an example of a function which we created and how to execute it (needs a call!)

```
def greeting(name):
    print("welcome on board " + name)

# if we execute this program now it would display nothing as we have not called this function

# syntax: to call function

greeting("Daniel")
calling our greeting function
this will execute the code inside the function
```




- create a new function that takes 2 arguments as ints and adds the value of the to args 





```
def add(num1, num2):
# creating an add function that takes 2 arguments
    print(num1 + num2)
# Display the sum of the arguments received

add(4, 5) 
```

- creating a subtraction function 

- num1 and num2 can be declared twice as they are part of two diff functions so do not appear as duplicates

```
def subtract(num1, num2):
# creating a function to subtract two arguments
    print(num1 - num2)

# calling function and passing two values

subtract(5, 2)
```


- This example below assign the call as a variable in order to smoothen the process of using the function and calling
- Return allows you to easily use the result of the function, it will also end the execution pf the function 


```
def subtract(num1, num2):
# creating a function to subtract two arguments
    return num1 - num2

subtracted_value = subtract(10,2)
# assigning call to a variable 

print(subtracted_value)
```



## Task

- create a function to *
- create a function to /
- create a function to %
- research return statement and use it instead of print in your functions
