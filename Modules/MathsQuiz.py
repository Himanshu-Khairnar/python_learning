import random
import math 
from timeit import default_timer as timer
correct = 0
wrong = 0
counter = 0
time = []
start = 0
end = 0

def question():
        global start
        start = timer()
        actions = ['+','-','/','*']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        action = actions[random.randint(0,3)]
        equation = f"{num1} {action} {num2}"
        print(f"equation: {equation}")
        return math.floor(eval(equation))
    
def evaluate(user_answer, evalu,time_taken):
    if(user_answer == answer):
        print(f"Correct Answer! Well done. and Time taken to answer the question is seconds {time_taken}")
        global correct
        correct =correct+ 1
    else:
        print(f"Wrong Answer! The correct answer is {answer} and Time taken to answer the question is seconds {time_taken}")
        global wrong
        wrong = wrong + 1
    global counter
    counter = counter + 1
        
        
def afterEqaution():
    afterEquationInput = int(input("Do you want to continue? 1: Yes 2: No 3.See Stats\n"))
    if(afterEquationInput==2):
        print(f"Game Over! You answered {correct} questions correctly and {wrong} questions wrongly out of {counter} questions.")
        exit()
    elif(afterEquationInput==1):
        return
    elif(afterEquationInput==3):
        average_time = sum(time)/len(time)
        print(f"Total Questions Answered: {counter}")
        print(f"Correct Answers: {correct}")
        print(f"Wrong Answers: {wrong}")
        print(f"Average Time per Question: {round(average_time,2)} seconds")
        afterEqaution()
while True:
    
    
            
    if(counter==0):
        print("Welcome to the Maths Quiz Game!")
        user = int(input("Enter the choice:\n 1. Start the Game \n 2. End the Game: \n"))
    
    if(user==1):
        answer = question()
        
        user_answer = float(input("Enter your answer: \n"))
        end = timer()
        print(end)
        print(start)
        time_taken = round(end - start, 2)
        time.append(time_taken)
        evaluate(user_answer, answer,time_taken)
        print(f"Current Score: {correct} correct, {wrong} wrong out of {counter} questions.")
        print("\n")
        afterEqaution()
        
   
        
        
    elif(user==2):
        print(f"Game Over! You answered {correct} questions correctly and {wrong} questions wrongly out of {counter} questions.")
        break
        
        
    
    
    