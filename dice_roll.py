# Any number other than 1 you get a chance to play & with each turn your no. on dice adds up to give the score.max_score
# If you get no. 1 it ends the game with score 0.
# Whoever scores 50 wins the game.
import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

# value=roll()
# print(value)

while True:
    players= input("Enter the number of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2-4")
    else:
        print("Invalid, Try again!")
# print(players)

max_score=50
player_scores = [0 for _ in range(players) ]
# print(player_scores)

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print("\nPlayer ",player_idx+1, "turn has just started!" )
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score=0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() !="y":
                break
    
            value = roll() 
            if value == 1:
                print("You got a 1. Turn done!")
                current_score=0
                break
            else:
                current_score += value
                print("You rolled a", value)
            print("Your score is: ",current_score)
            
        player_scores[player_idx] +=current_score
        print("Your total score is: ", player_scores[player_idx])
        
max_score = max(player_scores)
winnng_idx=player_scores.index(max_score)
print("Player number ", winnng_idx+1, "is the winner with max score of: ", max_score )