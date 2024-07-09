import logic

if __name__=='__main__':
    mat=logic.start_game()
    
while(True):
    x=input("Press the command: ")
    if(x=='W' or x=='w'):
        mat,flag=logic.move_up(mat)
        status=logic.current_state_matrix(mat)
        print(status)
        if status=='Game not over':
            logic.add_new2(mat)
        else:
            break
        
    elif(x=='S' or x=='s'):
        mat,flag=logic.move_down(mat)
        status=logic.current_state_matrix(mat)
        print(status)
        if status=='Game not over':
            logic.add_new2(mat)
        else:
            break
        
    elif(x=='A' or x=='a'):
        mat,flag=logic.move_left(mat)
        status=logic.current_state_matrix(mat)
        print(status)
        if status=='Game not over':
            logic.add_new2(mat)
        else:
            break
        
    elif(x=='D' or x=='d'):
        mat,flag=logic.move_right(mat)
        status=logic.current_state_matrix(mat)
        print(status)
        if status=='Game not over':
            logic.add_new2(mat)
        else:
            break
        
    else:
        print("Invalid key pressed")
    
    print(mat)