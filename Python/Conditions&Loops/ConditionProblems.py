# 1 Age Group Classification

# age = int(input("Enter your age: \n"))

# if(age<0):
#     print("Please enter correct age. ")
# elif(age<=13):
#     print("Child")
# elif( age<=19):
#     print("Teenager")
# elif( and age<=59):
#     print("Adult")
# else:
#     print("Senior")


# 2 Movie Ticket Generator

# age = int(input("Enter your age: \n"))
# day = input("Enter day of the week: \n")
# discount = 0
# price = 0
# if day == "Webnesday":
#     price -=2
# price = 12 if age>18 else 8


# print(f"Total price of ticket is {price}")


# Grade Assign

# marks = 101

# if marks>100 or marks<0:
#     print("Please enter valid marks")
#     exit()
# if(marks>89):
#     print("Grade A")
# elif(marks>79):
#     print("Grade B")
# elif(marks>69):
#     print("Grade C")
# elif(marks>59):
#     print("Grade D")
# else:
#     print("Fail")


# Banana Ripeness Checker

# ripness = "brown"

# if ripness == "green":
#     print("Unripe")
# elif ripness == "yellow":
#     print("Ripe")
# elif ripness == "brown":
#     print("OverRipe")


# Weather Activity Suggestion


# weather = "Sunny"

# if weather == "Sunny":
#     print("Go for a walk")
# elif weather == "Rainy":
#     print("Read a book")
# elif weather == "Snowy":
#     print("Build a snow man")

# Transportation mode selection

# distance =15

# if distance < 3:
#     print("Go for a walk")
# elif distance <15:
#     print("Go with Bike")
# elif distance>14:
#     print("go with a car")

# coffee customization

# size = "Medium"
# extraShot = True

# if extraShot:
#     print(f"Coffee of {size} size having an extra shot")
# else:
#     print(f"Coffee of  {size}")


#password Checher

# password = 'qwrdq12fejce'

# if len(password)>10:
#     print("Strong Password")
# elif 6<len(password)<=10:
#     print("Medium password") 
# else : print("Weak password")

#leap year

# year = 2025

# if year%400==0 or ( year% 4 ==0 and year%100!=0):
#     print("leap year")
# else: print("Not a leap year")

#pet dog food reccomadition

pet = 'dog'
age = 1

if pet == 'dog' and age <2:
    print("puppy food")
elif pet =='cat' and age>5:
    print("senior cat food")