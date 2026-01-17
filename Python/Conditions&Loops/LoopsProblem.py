import time
# count positive num

# numbers = [1, -2, 3, -4, 5, 6, 7, 8, 9, 10]
# count = 0
# for i in numbers:
#     if i>0:
#         count+=1

# print(f"Positive Number: {count}")


# sum of even num

# n = 10
# sum = 0

# for i in range(n + 1):
#     if i % 2 == 0:
#         sum += i

# print(f"Sum of even number is {sum}")


# multiplication table

# n = 5

# for i in range(1, n):
# for j in range(1, 11):
#     if j == 5:
#         continue
#     print(f"{i} x {j} = {i*j}")


# reverse a string

# string = "Himanshu"
# reversed_string = ""

# for i in string:
#     reversed_string =i + reversed_string

# print(reversed_string)


# first non-repeating char

# input_str = "helloh"

# for i in input_str:
#     if input_str.count(i) ==1:
#         print(f"element {i} is the first non repeated element")
#         break

# factorial

# num = 5
# fac = 1
# for i in range(1, num + 1):
#     fac *= i 
# print(fac)


#validate input

# while(True):
#     user = int(input("enter input btw 1 to 10: \n "))
#     if user >0 and user<11:
#         break


#prime number check

# num = 7
# isprime = True
# if num < 2:
#     isprime = False
# elif num ==2:
#     isprime = True
# elif num%2 ==0:
#     isprime = False
# else:
  
#     for i in range (3,int(num**0.5)+1,2):
#         if num%i ==0:
#             isprime = False
#             break
            
# print(f"{num} is prime: {isprime}")
        

#duplicate elements in list


# items =  ["apple", "banana", "orange", "mango"]

# for i in items:
#     if items.count(i) > 1:
#         print(f"duplicate element is: {i}")
#         break

# exponentiation backoff
time_delay = 1  # initial time delay in seconds 
tries = 5  # number of retries
while True:
    user = int(input("enter input btw 1 to 10: \n "))
    if user >0 and user<11:
        break
    else:
        print("invalid input, try again")
        time.sleep(time_delay)
        time_delay *= 2  
        tries -= 1
        if tries == 0:
            print("maximum retries reached. Exiting.")
            break