#Author: Sarika Dighe
#Date: 01/18/2020
#Solution for coding challenge

#A dedicated function to turn the ship to the left (90 degrees)
def Left(x, y, orient):
    if (orient == 'E'):
        orient='N'
    elif (orient == 'N'):
        orient='W'
    elif (orient == 'W'):
        orient='S'
    else:
        orient='E'
   
    return[x, y, orient];
    
    
#A dedicated function to turn the ship to the right (90 degrees)
def Right(x, y, orient):
    if (orient == 'E'):
        orient='S'
    elif (orient == 'N'):
        orient='E'
    elif (orient == 'W'):
        orient='N'
    else:
        orient='W'
   
    return[x, y, orient];
    
#A dedicated function to move the ship forward/backward
def Forward(x, y, orient,X_topright,Y_topright):
    if (orient == 'E'):
        x=x+1;
        y=y;
    elif (orient == 'N'):
        y=y+1;
        x=x;
    elif (orient == 'W'):
        x=x-1;
        y=y;
    else:
        y=y-1;
        x=x;
    if (x < X_topright and y < Y_topright):
        ship_status = ' '
    else:
        print("***Warning...Ship is LOST***")
        ship_status = 'LOST'
        
    return[x, y, orient,ship_status];
    

#Put everything together in the main block of the code

#First store inputs in the useful variables
    
def main():
    #Inputs for the problem:
    #Top-right corner of the grid
    first_line_input=input()
    [X_topright, Y_topright]=first_line_input.split()
    
    X_topright=int(X_topright) #X co-ordinate of the top right corner
    Y_topright=int(Y_topright) #Y co-ordinate of the top right corner

    #Ship initial position
    second_line_input=input()
    [x0, y0, orient0]=second_line_input.split() #Initial orientation of the ship for N S E W directions
    x0=int(x0) #X co-ordinate of the initial position of the ship
    y0=int(y0) #Y co-ordinate  of the initial position of the ship
    

    #Instruction for ship movement
    third_line_input=input() #String containing ship movement instruction
     

    data = list(third_line_input)
    x=x0
    y=y0
    orient=orient0

    #Loop through the instructions with one instruction at a time
    for temp in data:
        print(temp)
    
        if (temp == 'L'):
            print("Processing the instruction for 90 degree turn to the Left")
            [x, y, orient]=Left(x, y, orient); 
    
        elif (temp == 'R'):
            print("Processing the instruction for 90 degree turn to the Right")
            [x, y, orient]=Right(x, y, orient); 
        
        else:
            print("Processing the instruction for 'Forward' movement")
            [x, y, orient, ship_status]=Forward(x, y, orient,X_topright,Y_topright); 

    
    print(x, y, orient, ship_status)
    
if __name__ == '__main__':
    main()
