# def greet(name):
#     return f"hello, {name} !"

# print(greet("Anoj"))

# def add():
#     return f"{2 + 1}"

# print(add())


#----------------- functions in python --------------------------
#example 1:
def hello_func():
    pass # it will never print anything

print (hello_func())
print(hello_func)
#output : None
# <function hello_func at 0x0000014914E8D080>

#exmple 2:
def hi_function():
    print("hi !")

hi_function()

#example 3 : Returning statement
def hello_function():
    return "Hello Anoj"

print(hello_function())
print(hello_function().upper())

#example 4 : Passing arguments
def hello_function(greeting, name):
    # return f"{greeting} {name} !"
    return '{} {}!'.format(greeting, name)

print(hello_function("Hello", "Anoj").upper())

# ---------------------------------------------------------
def student_info(*args, **kwargs): #any name can be used instead of args and kwargs
    print(args) #arbitary arguments
    print(kwargs) #keyword arguments

course = ['Math', 'Physics'] # * used to unpack the list
info = {'name': 'Anoj', 'age': '22'} # ** used to unpack the dictionary
# student_info('Math', 'physics', name = 'Anoj', age = '22')
student_info(*course, **info)


#Final Exmaple which include all 

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def  is_leap(year):
    """Return True for leap years, False for non-leap years.""" #docstring alsways use in side function is good pratice 
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]


print(days_in_month(2024, 6))
print(is_leap(2024))
