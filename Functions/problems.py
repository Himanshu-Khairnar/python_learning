import math

#return sqaure of a number
def squareNum(num):
    return num**2

# print(squareNum(3))

def Sum(num1,num2):
    return num1+num2

# print(Sum(1,2))

#string multiplications

def mul(num1,num2):
    return num1*num2

# print(mul(2,'g'))

def circle(radius):
    area = (radius**2) * math.pi    
    perimeter = (radius*2) * math.pi    
    return round(area,2),round(perimeter,2)


# area,circumfernece = circle(4)
# print(f"Area: {area} and Circumfernece: {circumfernece}")

def greet(name="Himanshu"):
    print(f"Hello {name}")

# greet() 


cube = lambda x: x**3

# print(cube(2))

def sum_all(*args):
    print(type(args))
    for i in args:
        print(i**2)
    return sum(args)

# print(sum_all(1,2,3,4))

def kwargsuse(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} {value}")

# kwargsuse(name="himanshu",age=20,college="sangavi")

def even(limit):
    for i in range(2,limit+1,2):
        yield i
        
# for i in even(10):
#     print(i)
        

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
