import random 
import numpy as np
from collections import deque


playingBoard =np.array([[0,0,0,0]
                       ,[0,0,0,0]
                       ,[0,0,0,0]
                       ,[0,0,0,0]])



#initializing Starting points for the first 2s twos to appear
ad1 = (random.sample(range(0, 4),2))
ad2 = (random.sample(range(0,4),2))
firstndex = (ad1[0],ad2[0])
secondtndex = (ad1[1],ad2[1])


#placing starting points on board 
playingBoard[firstndex] = 2
playingBoard[secondtndex] = 2

# for i in range(4):
#     pass
#     print(playingBoard[i])





#Shifts all non zero elements of an array to the left

def ArrayShiftL(arr):
    global shiftDone
    shiftDone = False
    nonzero= [] 

    ZeroLocaction = [] # Where zero lies by location 
    for i in range(4):
        
        if arr[i] == 0:
            ZeroLocaction.append(i)  # appned index of zero
            
        
        if arr[i] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
                shiftDone = True
                arr[ZeroLocaction[0]]= arr[i] #first zero replaced
                arr[i] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i)
            
                 
def ArrayShiftAddL(arr):
  
    nonzero= [] # Where non zero lies by index
    ZeroLocaction = [] # Where zero lies by index
    global addDone
    addDone = False # only add numbers once per turn 
    
    for i in range(4):
        # print(nonzero)
        # print(ZeroLocaction)
        # print(addDone)
        if arr[i] == 0:
            ZeroLocaction.append(i) # if cuurent element zero append its location


        if arr[i] != 0: #non zero number
            
            if nonzero != [] and addDone == False:
                if i - nonzero[-1] == 1:  #check if last non zero element  and current  elemenst together
                  
                
                    if arr[nonzero[-1]] == arr[i]: # if same
                    
                        addDone = True
                    
                        arr[nonzero[-1]]+= arr[i]
                        arr[i] = 0 
                        del nonzero[0]
                        ZeroLocaction.append(i)
                    else: # if elements not equal append to non zero list
                        nonzero.append(i)
            
            else:
                nonzero.append(i)
                    
        if arr[i] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
            
                arr[ZeroLocaction[0]]= arr[i] #first zero and current element swap
                arr[i] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i) 
              

def ArrayShiftR(arr):
    nonzero= [] 
    global shiftDone
    shiftDone = False

    ZeroLocaction = [] # Where zero lies by location 
    for i in range(3,-1,-1):
        
        if arr[i] == 0:
            ZeroLocaction.append(i)  # appned index of zero
            
        
        if arr[i] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
                shiftDone = True
                arr[ZeroLocaction[0]]= arr[i] #first zero replaced
                arr[i] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i)
            
        

def ArrayShiftAddR(arr):
   
    nonzero= []
    ZeroLocaction = [] # Where zero lies by location 
    global addDone
    addDone = False
    
    for i in range(3,-1,-1):
        if arr[i] == 0:
            ZeroLocaction.append(i) # if cuurent element zero append its location

        if arr[i] != 0: #non zero number
            
            if nonzero != [] and addDone == False and nonzero[-1] - i == 1:  #check if last non zero element  and current element together
                
                if arr[nonzero[-1]] == arr[i]:
                    
                    addDone = True
                
                    arr[nonzero[-1]]+= arr[i]
                    arr[i] = 0 
                    # del nonzero[0]
                    ZeroLocaction.append(i)
                else:
                    nonzero.append(i)
            
            else:
                nonzero.append(i)
                    
                    
                    
        if arr[i] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
            
                arr[ZeroLocaction[0]]= arr[i] #first zero replaced
                arr[i] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i)
    
    

 
    


# testing playing board examples 
# playingBoard =np.array([[2,4,2,4]
#                        ,[4,4,2,4],
#                         [0,0,0,2]
#                        ,[0,0,0,0]])

# playingBoard =np.array([[0,0,0,0]
#                        ,[4,0,0,0],
#                         [2,4,0,4]
#                        ,[2,2,4,4]])




print(playingBoard)
#  row * column  



def ArrayShiftUp(column,testBoard):
    # for i in range(4):
    #     # print("check",testBoard[i,column])
        
    nonzero= [] 
    global shiftDone
    shiftDone = False

    ZeroLocaction = [] # Where zero lies by location 
    for i in range(4):
        
        if testBoard[i,column] == 0:
            ZeroLocaction.append(i)  # appned index of zero
            
        
        if testBoard[i,column] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
                shiftDone = True
            
                testBoard[ZeroLocaction[0],column]= testBoard[i,column] #first zero replaced
                testBoard[i,column] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i)






def ArrayShiftUpAdd(column,testBoard):
    nonzero= []
    ZeroLocaction = [] # Where zero lies by location 
    global addDone
    addDone = False
    
    for i in range(4):
        # print(testBoard[i,column])
       
        if testBoard[i,column] == 0:
            ZeroLocaction.append(i) # if cuurent element zero append its location


        if testBoard[i,column] != 0: #non zero number
            
            if nonzero != [] and addDone == False and i - nonzero[-1] == 1:  #check if not first non zero element  and if elemenst together
                if testBoard[nonzero[-1],column] == testBoard[i,column]:
                    addDone = True
                
                    testBoard[nonzero[-1],column]+= testBoard[i,column]
                    testBoard[i,column] = 0 
                    # del nonzero[0]
                    ZeroLocaction.append(i)
                else:
                    nonzero.append(i)
            else:
                nonzero.append(i)
                    
                    
                    
        if testBoard[i,column] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
            
                testBoard[ZeroLocaction[0],column]= testBoard[i,column] #first zero replaced
                testBoard[i,column] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i)
                


def ArrayshiftDown(column,testBoard):
    # for i in range(4):
    #     # print("check",testBoard[i,column])
    global shiftDone
    shiftDone = False
    nonzero= [] 

    ZeroLocaction = [] # Where zero lies by location 
    for i in range(3,-1,-1):
        
        if testBoard[i,column] == 0:
            ZeroLocaction.append(i)  # appned index of zero
            
        
        if testBoard[i,column] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
                shiftDone = True
                testBoard[ZeroLocaction[0],column]= testBoard[i,column] #first zero replaced
                testBoard[i,column] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i)




def ArrayShiftDownAdd(column,testBoard):
    nonzero= []
    ZeroLocaction = [] # Where zero lies by location 
    global addDone
    addDone = False
    
    for i in range(3,-1,-1):
        
       
        if testBoard[i,column] == 0:
            ZeroLocaction.append(i) # if cuurent element zero append its location


        if testBoard[i,column] != 0: #non zero number
            
            if nonzero != [] and addDone == False and  nonzero[-1]-i  == 1:  #check if not first non zero element  and if elemenst together
                if testBoard[nonzero[-1],column] == testBoard[i,column]:
                    addDone = True
                
                    testBoard[nonzero[-1],column]+= testBoard[i,column]
                    testBoard[i,column] = 0 
                    del nonzero[0]
                    ZeroLocaction.append(i)
                else: 
                    nonzero.append(i)
            
            else:
                nonzero.append(i)
                    
                    
                    
        if testBoard[i,column] != 0:
            if ZeroLocaction != []: # if  zero exists behind current non zero number 
            
                testBoard[ZeroLocaction[0],column]= testBoard[i,column] #first zero replaced
                testBoard[i,column] = 0 
                del ZeroLocaction[0]
                ZeroLocaction.append(i)
                



def main():
   
    keypress = ""
    while keypress.lower() != "e":
        boardChanged = False
        keypress = input("enter key or exit: ")
        
        
        if keypress== "a":
            for i in range(4):
                ArrayShiftL(playingBoard[i])
                ArrayShiftAddL(playingBoard[i])
                if addDone == True:
                    boardChanged = True
                if shiftDone == True:
                    boardChanged = True
            
        elif keypress== "d":
            for i in range(4):
                ArrayShiftR(playingBoard[i])
                ArrayShiftAddR(playingBoard[i])
                if addDone == True:
                    boardChanged = True
                if shiftDone == True:
                    boardChanged= True
        
                 
        elif keypress =="s":
            for i in range(4):
                ArrayshiftDown(i,playingBoard)
                ArrayShiftDownAdd(i,playingBoard)
                if addDone == True:
                    boardChanged = True
                if shiftDone == True:
                    boardChanged= True
        
            
             
        elif keypress =="w":
            for i in range(4):
                ArrayShiftUp(i,playingBoard)
                ArrayShiftUpAdd(i,playingBoard)
            if addDone == True:
                boardChanged = True
            if shiftDone == True:
                boardChanged= True
    
             
                
        elif keypress !="e":
            print("Enter Valid WASD Key")
            
            
        solutions = np.argwhere(playingBoard == 0)
        randomSol = random.choice(solutions)
        
        x = randomSol[0]
        y = randomSol[1]
        if boardChanged == True:

            playingBoard[x,y]= 2
        print("Changed to \n",playingBoard) 
        print("board Change", boardChanged)
        

   
            

main()


            





# import numpy package


# create an numpy array 
