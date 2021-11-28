# A Quiz Game in Python
print('Welcome to Python Quiz')
answer = input('Are you ready to play the Quiz? (yes/no) :')
score = 0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question Number 1: What is your Favourite programming Language?')
    if answer.lower()=='Python':
        score +=1
        print('correct')
    else:
        print('Wrong Answer:(')

    
    answer=input('Question Number 2: Do you follow any author on AskPython?')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer:')
    
    answer=input('Question Number 3: What is your favourite website?')
    if answer.lower()=='askpython':
        score += 1
        print('correct')
    
    else:
        print('Wrong Answer:(')

print('Thankyou for playing this game, you attempted', score,"questions correctly.")
mark=(score/total_questions)*100
print('Marks obtained:', mark)
print('Thank you!')