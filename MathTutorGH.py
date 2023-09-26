import random

fail = ""
success = ""
choice = "y"

while choice == "y":
   
    #changed parameters from (0,9) to (1,10) to avoid division by 0
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    randmsg = random.randint(0, 3)
    op = random.choice(['+', '-', '*', '*'])
    
    if op == '+': 
        answer = num1 + num2   
    elif op == '-': 
        answer = num1 - num2
    elif op == '*': 
        answer = num1 * num2  
    elif op == '/': 
        answer = num1 / num2

    #We could also put responses into a list and just shuffle(randmsg)
    if randmsg == 0:
        success = "Well done"
        fail = "Don't give up"
    elif randmsg == 1:
        success = "Excellent"
        fail = "Hang in there"
    elif randmsg == 2:
        success = "Rock on"
        fail = "Incorrect. Once more"
    elif randmsg == 3:
        success = "Keep up the good work"
        fail = "Wrong. Try again"
    else:
        print("An error occurred")

    # Prompt the user to enter an answer
    print(f"What's {num1} {op} {num2}?")
    user_answer = int(input())   
    if user_answer == answer: 
        print(success)
    else:
        print()
        print(fail)
        print(f"The correct answer is {answer}")

    print()
    choice = input("Continue? (y/n): ")
