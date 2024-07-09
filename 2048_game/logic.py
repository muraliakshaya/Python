# 4*4 matrix with addition of powers of 2
import random

#function to initialize game
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
        
    print("Commands are as follows:  ")
    print(" 'W' or 'w' : Move up")
    print(" 'S' or 's' : Move down")
    print(" 'A' or 'a' : Move left")
    print(" 'D' or 'd' : Move right")
    
    add_new2(mat)
    return mat

#function to add 2 in the game
def add_new2(mat):
    #choosing random index for row & column
    r= random.randint(0,3)
    c= random.randint(0,3)
    
    #while loop breaks as selected index is 0
    while(mat[r]!=0):
        r= random.randint(0,3)
        c= random.randint(0,3)
    #placing 2 at empty random cell
    mat[r]=2
    
# function to understand current state of matrix
def current_state_matrix(mat):
    # if game won
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==2048):
                # print("You won")
                return "You WON"
            
    # if game not over withatleast one cell empty
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==0):
                # print("Game not over")
                return "Game not over"
            
    #if no empty cell but possibility to merge 2 cells
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i+1][j] or mat[i][j]==mat[i][j+1]):
                return "Game not over"
            
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return "Game not over"
        
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "Game not over"
        
    return "You lose!"

#compress the grid
def compress(mat):
    #toevaluate if any change
    changed= False
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                
                if(j!=pos):
                    changed=True
                pos +=1
                
    return new_mat,changed

#merge the elements
def merge(mat):
    changed= False
    for i in range(4):
        for j in range(3):
            if (mat[i][j]==mat[i][j+1] and mat[i][j]!=0):
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
                changed= True
    return mat,changed

# find reverse of elements in sequence of the matrix
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range (4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

#find transpose of the matrix
def transpose(mat):
    new_mat=[]
    for i in range (4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

#function to update the matrix on moving to left
def move_left(grid):
    #compress the grid
    new_grid, changed1=compress(grid)
    #merge the grid
    new_grid, changed2=merge(new_grid)
    
    changed= changed1 or changed2
    #compress again after merging
    new_grid, temp=compress(new_grid)
    return new_grid, changed

#function to update the matrix on moving to right
def move_right(grid):
    #reverse the matrix to move right
    new_grid=reverse(grid)
    #move the matrix to left
    new_grid, changed= move_left(new_grid)
    #again reverse the matrix to get desired matrix which is moved to right
    new_grid=reverse(new_grid)
    return new_grid,changed

def move_up(grid):
    #transpose the matrix to move up
    new_grid= transpose(grid)
    new_grid, changed= move_left(new_grid)
    new_grid=transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid= transpose(grid)
    new_grid,changed= move_right(new_grid)
    new_grid= transpose(new_grid)
    return new_grid, changed


        
                
            
    
                
    
    
        
    
        
    