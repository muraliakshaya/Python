#LOGIC count 1-21,21-eliminated
# The player can choose to start first or second.
# The list of numbers is shown before the Player takes his turn so that it becomes convenient.
# If consecutive numbers are not given in input then the player is automatically disqualified.
# The player loses if he gets the chance to call 21 and wins otherwise.

   
"""         STEPS
1.The code starts by creating an empty list, xyz.
2.It then checks to see if the number 4 is in the list.
3.If it is not, the code adds 4 to num and continues checking numbers.
4.If num is equal to or greater than 4, the code calculates the nearest multiple of 4 and stores that value in near.
The code then prints “YOU LOSE!”
and ends the game.
If num is not equal to or greater than 4, the code checks to see if xyz[i] – xyz[i-1] equals 1.
If it does not, then i has incremented by 1 and check() returns False so last can be set to i instead of 0 (last = i).
Otherwise, i has incremented by 1 and check() returns True so last can be set to i+1 instead of len(xyz)-1 (last = len(xyz)+1).
The start() function starts the game by assigning xyz[] a new length of zero.
This will cause last to always return 0 because there are no numbers yet in xyz[] .
The code starts by creating an empty list, last in particular will keep track of the player’s score.
Next, a while loop is started which will run until the user presses CTRL+C.
This while loop will be responsible for playing the game.
Inside the loop, xyz will be set to an empty list.
The len function will be used to determine how many numbers are in xyz .
Next, i will be set to 1 and it’ll start counting from 0 .
The check function is then called which checks whether each number in xyz is consecutive.
If it isn’t, false is returned and i is incremented by 1 .
If all numbers are consecutive, then True is returned and i is reset to 1 .
The code starts by asking the player for a number between 1 and 20.
If the player enters a number that is not between 1 and 20, then the program prints “Your Turn.”
The code then asks the player how many numbers they want to enter.
If the player enters a number greater than 0 and less than 3, then the program calculates their chance of winning as 4 – input().
If the player enters a number greater than 3, then their chance of winning is input().
The if statement checks to see if last equals 20.
If it does, then lose1() is called.
Otherwise, print(“Your Turn.”)
and ask for another number from the player.
The while True: loop will keep running until either someone inputs a number other than “Your Turn” or last equals 20 again.
In this loop, if last equals 20 again, then lose1() is called; otherwise, print(“\nHow many numbers do you wish to enter?”)
and allow the player to enter another number.
Inp is used in both if statements because it stores whatever was entered by the user (in this case, numbers).
int(input(‘> ‘)) converts that string into an integer so that it can be
The code will ask the player for a number between 0 and 3.
If the number entered is greater than 0 but less than 3, then the code will check to see if the player has input 4 – the number they entered.
If not, then the code will check to see if the player has input a number that equals 4.
If so, then it will use that number as their comp value.
If the player enters a number that does not equal 4, then they will be asked to enter another number.
The game will keep track of how many numbers have been entered by the player and once they have input three numbers or more, it will declare them as losing and display an appropriate message on-screen.
The code starts by initializing two variables, i and j.
The code then prints a message telling the player that they are disqualified from the game because they entered an invalid input.
Next, the code loops through the input string and assigns each character to a variable.
The first loop checks whether each number is a consecutive sequence.
If it is, then the code stores the last number in last variable and continues with the next loop.
Otherwise, if check() returns True, then the player has entered an invalid input and loses 1 point.
In this example, there are three possible outcomes of this game: (1) Player enters 21 as their input; (2) Player enters 22 as their input; or (3) Player enters any other valid input besides 21 or 22.
In all three cases, if player loses due to an invalid input, they will be given a message indicating what happened and where to find more information about Python programming concepts.
The code will check whether the input numbers are consecutive and, if they are, it will print “Wrong input.
You are disqualified from the game.” If the input numbers are not consecutive, then it will print “Now enter the values” and ask the player to enter a number between 1 and 20.
Once the player enters a number, it will append that number to xyz and increment i by 1.
The last element of xyz will be stored in last and checked to see if it is equal to 21.
If it is, then lose1() is called and the game is over.
Otherwise, the game continues.
The code starts by declaring two variables: comp and last.
comp is a variable that stores the number of times the computer has turned, and last stores the number entered by the player.
The code then declares two functions: lose1() and near.
lose1() is a function that will be used to determine if the player has lost (i.e., if their input does not match any of the inputs in xyz).
near is a function that will be used to determine whether or not there are any multiple matches for the player’s input (in other words, it will return the nearest multiple of 20).
Next, the code sets up an infinite loop in which comp keeps track of how many times the computer has turned, and last keeps track of what was entered by the player.
The while loop inside this loop checks to see if game is True (which it always is at first), and then it runs different parts of code based on that condition.
First, if game is False (which means that someone else has won), then lose1() determines whether or not they have lost (by checking to see if their input matches any in xyz).
If they have lost, then they exit out of this program with an
The code will keep track of the order in which the players input integers.
The player will have two chances to input integers.
If they input consecutive integers, they are automatically declared the winner.
If they make a mistake, they have a second chance to input integers.
If they still make a mistake, they are disqualified from the game.
If the player inputs incorrect values, their turn is over and the computer takes over again.
The code also prints out congratulatory messages to the player once they win and displays an error message if there is a problem with playing the game.

    """
    
def nearestMultiple(num):
    if num>=4:
        near=num+(4 - (num%4))
    else:
        near=4
    return near


def lose():
    print ("\n\nYOU LOSE !")
    print("Better Luck next time!")
    exit(0)

def check_consecutive():
    i=1
    while i< len(xyz):
        if(xyz(i)-xyz(i-1)!=1):
            return False
            i=i+1       
        return True
   
def start_game():
    xyz=[]
    last=0
    while True:
        print("Enter 'First' to take first chance")
        print("Enter 'Second' to take second chance")
        chance=input('>')
        
        # player takes the first chance
        if chance=='First':
            while True:
                if last==20:
                    lose()
                else:
                    print ("\nYour Turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    input_number=int(input('>'))
                    if input_number>0 and input_number<=3:
                        comp= 4 - input_number
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose()
                        
                    i,j = 1,1
                    print("Now enter the values:- ")
                    while i< input_number:
                        a = input('> ')
                        a=int(a)
                        xyz.append(a)
                        i=i+1 
                    # store the last element of xyz.
                    last=xyz[-1]
                    if check_consecutive(xyz)== True: 
                        if last==21:
                            return lose()   
                        else:
                            "Computer's turn"
                            while j<= comp:
                                xyz.append(last + j)
                                j = j+1
                            print("Order of input after computer's turn is")
                            print(xyz)
                            last= xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose()
                        
        # if player takes second chance
        elif chance== 'Second':
            comp=1
            last=0
            while last<20:
                j=1
                while j<=comp:
                    xyz.append(last + j)
                    j=j+1
                print("Order of input after computer's turn is:-")
                print(xyz)
                if (xyz[-1]==20):
                    return lose()
                else:
                    print ("\nYour Turn.")
                    print ("\nHow many numbers do you wish to enter? ")
                    input_number = input('> ')
                    input_number =int(input_number)
                    i=1
                    print("Enter your values: ")
                    while i<=input_number:
                        xyz.append(int(input(">")))
                        i=i+1
                    last=xyz[-1]
                    if check_consecutive(xyz)== True:
                        print(xyz)
                        near= nearestMultiple(last)
                        comp= near -last
                        if comp==4:
                            comp=3
                        else:
                            comp=comp
                    else:
                        print ("\nYou did not input consecutive integers.")
                        lose()
						# print ("You are disqualified from the game.")
            print ("\n\nCONGRATULATIONS !!!")
            print ("YOU WON !")
            exit(0)
        else:
            print ("wrong choice")
            
game = True
while game==True:
    print ("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans=input('>')
    if ans=='Yes':
        start_game()
    else:
        print ("Do you want quit the game?(yes / no)")
        nex=input('>')
        if nex=='Yes':
            print ("You are quitting the game...")
            exit(0)
        elif nex=='No':
            print ("Continuing...")
        else:
            print("Wrong choice!")
            
            
            

                        
                    
                    
                    
                    
        
                                               

                
                    
                    
