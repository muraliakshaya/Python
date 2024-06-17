import math
import random

lower=int(input("Enter lower bound:- "))
upper=int(input("Entr upper bound:- "))
#generated random number
x= random.randint(lower,upper)
print("\n\t You have only ", round(math.log(upper-lower + 1,2)),"chances to guess the number!")

#initial guess
count = 0
#guessing the range
while count<math.log2(upper-lower+1):
    count +=1
    guess=int(input("Guess a number:- "))
    
    #TESTING CONDITIONS
    
    if x==guess:
        print("Congratulations you did it in ",count," try!")
        break
        
    elif x<guess:
        print("You guessed it too high!")
    elif x>guess:
        print("You guessed it too small!")

# If more guesses required
if count>=math.log2(upper-lower+1):
    print("\nThe number is %d" %x)
    print("\t Better luck next time!")