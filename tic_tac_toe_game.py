import random
def check(player,position):
    '''Checks whether the input position is valid or not.
    A position is valid only if it is from 1 to 9 and not ocuupied by another player.
    '''
    if position in "123456789" and dict[position]=="_":
        if player==1:
            dict[position]="O"
        else:
            dict[position]="X"
        printdict(player)
    else:
        if player==2:
            position=str(random.randint(1,10))
            check(player,position)
        else:
            position=str(input("Please enter valid position: "))
            check(player,position)

def winner(player):
    if dict["1"]==dict["2"]==dict["3"]!="_" or dict["4"]==dict["5"]==dict["6"]!="_" or dict["7"]==dict["8"]==dict["9"]!="_" :
        #checks if all elements in a row are equal  
        print(f"Player {player} is winner")
        return True
    if  dict["1"]==dict["5"]==dict["9"]!="_" or dict["3"]==dict["5"]==dict["7"]!="_":
        #checks if all elements in a diagonal are equal
        print(f"Player {player} is winner")
        return True
    if dict["1"]==dict["4"]==dict["7"]!="_" or dict["2"]==dict["5"]==dict["8"]!="_" or dict["3"]==dict["6"]==dict["9"]!="_" :
        #checks if all elements in a column are equal
        print(f"Player {player} is winner")
        return True

def printdict(player=1):
    #prints the tic-tac-toe game
    if player==2:
        print("Player 2 Turn: ")
    n=9
    for i in range(1,n+1):
        print(dict[str(i)],end=" ")
        if i%3==0:
            print()
    print()
        
dict={"1":"_","2":"_","3":"_","4":"_","5":"_","6":"_","7":"_","8":"_","9":"_"}
iswinner=False
printdict()
for i in range(1,10):
    if i%2!=0:
        position=str(input("Enter postion: "))

        check(1,position)
        if winner(1):
            iswinner=True
            break
    else:
        position=str(random.randint(1,10))
        check(2,position)
        if winner(2):
            iswinner=True
            break
if not iswinner:
    print("Its a tie")