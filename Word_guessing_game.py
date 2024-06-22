import random

name=input("Enter your name? ")
print("Good Luck",name)

words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=random.choice(words)
print("Guess the characters: ")
guesses = ' '
turns=12

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed +=1 
            
    if failed==0:
        print("Congrats,You got the word!- ", word)
        break
    print( )
        
    guess=input("Guess a character! ")
    guesses += guess
    if guess not in word:
        turns-=1
        print("Wrong guess!")
        print("You have ",turns, "more chances! ")
        if turns==0:
            print("Game Over! The word was ",word)
            