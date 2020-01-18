#Author: Sarika Dighe
#Date: 01/18/2020
#Solution for coding challenge: Survey of Ships


lost_coords=set() #Global set variable to store a set of lost-co-ords and orientation of ships

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
    global lost_coords
    skip_flag = False
    
    if (x, y, orient) in lost_coords:
        print("""***Co-ords are ({}, {}, {}) are found in lost-cordinate list 
              from previous ship(s), thus skipping the instruction***""".format(x,y,orient))
        skip_flag=True
        ship_status=' '
        
    if skip_flag == False:        
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
        if ((x >= X_topright and orient== 'E') or (y >= Y_topright and orient== 'N')):
            ship_status = 'LOST'
            print("*****Warning...Ship is LOST*****")
            lost_coords.add((x, y, orient))
        else:
            ship_status = ' '            
        
    return[x, y, orient,ship_status]
    
 #Put everything together in the main block of the code   
def main():
    #Inputs for the problem:
    print("***This is a ship survey system***")
    print("\nInputs for ship navigation")
    print("\nEnter top right corner X & Y co-ordinates of the grid:\n")
    first_line_input=input()
    [X_topright, Y_topright]=first_line_input.split()
    
    X_topright=int(X_topright) #X co-ordinate of the top right corner
    Y_topright=int(Y_topright) #Y co-ordinate of the top right corner
    
    if (X_topright > 50 or Y_topright > 50):
        print("***Error! Grid co-ordinate value(s) are more than 50! Program exiting! ***")
        return

    repeat_navigate=True
    while (repeat_navigate==True):
        #Ship initial position
        print("\nEnter initial position and orientation of the ship:\n")
        second_line_input=str(input()).upper()
        [x0, y0, orient0]=second_line_input.split() #Initial orientation of the ship for N S E W directions
        x0=int(x0) #X co-ordinate of the initial position of the ship
        y0=int(y0) #Y co-ordinate  of the initial position of the ship
    

        #Instruction for ship movement
        print("\nEnter instructions for the ship:\n")
        third_line_input=str(input()).upper() #String containing ship movement instruction
     
        if (len(third_line_input)>=100):
            print("***Error! Instruction string legnth is 100 or greater! Program exiting! ***")
            return
            
        data = list(third_line_input)
        x=x0
        y=y0
        orient=orient0

        #Loop through the instructions with one instruction at a time
        for temp in data:
        
    
            if (temp == 'L'):
                print(temp, ": Processing the instruction for 90 degree turn to the Left")
                [x, y, orient]=Left(x, y, orient); 
    
            elif (temp == 'R'):
                print(temp, ": Processing the instruction for 90 degree turn to the Right")
                [x, y, orient]=Right(x, y, orient); 
        
            else:
                print(temp, ": Processing the instruction for 'Forward' movement")
                [x, y, orient, ship_status]=Forward(x, y, orient,X_topright,Y_topright)
                if ship_status == 'LOST':
                    break

        print("\n******************************\n")
        print("\nFinal Position of the ship is:\n")
        print(x, y, orient, ship_status)
        print("\n******************************\n")
        
        option=str(input("\nDo you want to perform navigation on another ship? (Y/N)")).upper()
        if option == 'Y':
            repeat_navigate=True
        else:
            repeat_navigate=False
            
    
if __name__ == '__main__':
    main()
