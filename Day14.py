#quiz game
    
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)

        check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    
#---------------------------    
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG!")
        return 0

#---------------------------
def display_score(correct_guesses, guesses):
    print("---------------")
    print("RESULTS")
    print("---------------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#---------------------------
def play_again():

    response = input("Do you want to play again?(yes or no): ").upper()

    if response == "YES":
        return True
    else:
        return False
#---------------------------
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerburg"],
           ["A. 1989","B. 19991","c. 2000","D. 2016"],
           ["A. Lonely Island", "B. Smosh", "3. Monty Python", "D. SNL"],
           ["A. True","B. False","C. sometimes","D. What's Earth"]]

new_game()

while play_again():
    new_game()

print("Byeee!")

"""---------------
Who created Python?: 
A. Guido van Rossum
B. Elon Musk
C. Bill Gates
D. Mark Zukerburg
Enter (A, B, C, D): a
CORRECT
---------------
What year was Python created?: 
A. 1989
B. 19991
c. 2000
D. 2016
Enter (A, B, C, D): B
CORRECT
---------------
Python is tributed to which comedy group?: 
A. Lonely Island
B. Smosh
3. Monty Python
D. SNL
Enter (A, B, C, D): C
CORRECT
---------------
Is the Earth round?: 
A. True
B. False
C. sometimes
D. What's Earth
Enter (A, B, C, D): D
WRONG!
---------------
RESULTS
---------------
Answers: ABCA
Guesses: ABCD
Your score is: 0%
Do you want to play again?(yes or no): noo
Byeee!
"""
