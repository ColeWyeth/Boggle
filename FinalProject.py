#first I'll write a function taking in an array of numbers
#and a word and checking if the word is "in" the array.

##########
# BOGGLE #
##########

import random
import string

die =  ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY", "EIOSST", "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ", "DELIRX"]

Grid = []   #generates grid. I stupidly forgot that there are various different die with different frequencies of numbeers, but I'll fix that later. 
remainingDie = 16 #because dice are eliminated as they roll
for i in range(16):
    if len(die) ==1:
        num = 0
    else:
        num = random.randrange(0,remainingDie-1)
    roll = random.randrange(0,5)
    Grid.append(die[num][roll])
    die.pop(num)
    remainingDie-=1

    
    
#DON'T FORGET THIS!!!!
listOfWords = open("dictionaryForBoggle.txt","r") #IMPORTANT!
                                                  #This line must be changed
boggleWords = []                                  #if in a different directory

for line in listOfWords:
    boggleWords.append(line.upper().strip())

    
def findNextLetter(letter, position,Grid, beenUsed):
    '''Takes in the current position, a Grid, and a letter to look for. Outputs all adjacent positions of the letter. If there are none, outputs []. '''
    closeLetters = {0:[1,5,4], 1:[0,4,5,6,2],2:[1,5,6,7,3],3:[2,6,7],4:[0,1,5,8,9],5:[0,1,2,6,10,9,8,4],6:[1,2,3,7,11,10,9,5],7:[2,3,11,10,6],8:[4,5,9,13,12],
                    9:[4,5,6,10,14,13,12,8],10:[5,6,7,11,15,14,13,9],11:[6,7,15,14,10],12:[8,9,13],13:[8,9,10,14,12],14:[9,10,11,15,13],15:[10,11,14]} 
    letterPositions=[] #will store where the letter is found. 
    for square in closeLetters[position]: #loops over all squares adjacent ("close") to the position. 
        if(Grid[square]==letter and beenUsed[square]==False): #checks if this particular square in the grid has the letter in it. 
                    letterPositions.append(square)
    return(letterPositions)

def wordFinder(word, number, positions, Grid, beenUsed): #this looks complicated but is really pretty simple. 
    '''Takes in the word overall being searched for, the number of the letter that we're looking for, the list of starting positions, and the Grid. If the word is 
    found, returns true. Otherwise, returns false. '''   
        
    if positions == []: #if no occurences of the LAST letter looked for were found, this is a dead end. 
        return False
    elif number == len(word): #if this condition is met, the word has been found. Otherwise, false would have been returned by now. 
        return True
    else:
        for position in positions:
            beenUsed[position] = True
            if(wordFinder(word, number+1, findNextLetter(word[number], position, Grid, beenUsed), Grid, beenUsed)): #find next letter should just return the list for the next letter
               return(True) #if any of the wordFinders called by this wordFinder (whether or not it is the original) returned True, it returns True.
               #therefore, if the word is found, the top function will be True.
            beenUsed[position] = False
        return(False) #if we get to this point, the function has not returned True and must return False.    
        
        
def wordCheck(word, Grid):
    """Checks to see if a word is 'in' a grid by Boggle rules. Takes in a list
    and a string, and outputs a boolean."""
    
    #The grid is encoded as:
    # 00 01 02 03
    # 04 05 06 07
    # 08 09 10 11
    # 12 13 14 15
    #this could be replaced with vectors in the vertical and horizontal directions and distance calculations, but as it is the method is very straightforward.

    nextLetter = [] #will store all positions of the next letter that is being searched for.
    for i in range(16):  #the purpose of this sequence is just to initialize nextLetter to the occurences of the first letter. 
        if(Grid[i] == word[0]):
            nextLetter.append(i)
    
    usedList = 16*[False]

    if (wordFinder(word, 1, nextLetter, Grid, usedList)): #Note: I will add checking against a dictionary here. 
        return True
    else: return False
        
#OK, so on to generating the grid. I already wrote the code for the grid above. 
        
for i in range(16):
        print("\t" + str(Grid[i]),end = "")
        if (i%4==3):
                print("\n")                  
score = 0            
done = False

alreadyUsed =[]
while done == False:   #there appears to be a runtime error. I'll fix it latter. 
        word = input("Enter a word?").upper()
        if wordCheck(word, Grid) and (word in boggleWords) and len(word)>2 and word not in alreadyUsed:
                if(len(word)<5):
                    score+=1
                elif(len(word<6)):
                    score+=2
                elif(len(word<7)):
                    score+=3
                elif(len(word<8)):
                    score+=5
                elif(len(word>7)):
                    score+=11
                alreadyUsed.append(word)
                answer = input("Good job! You're score is "+str(score)+"."+" Are you done?")
                if(answer == "yes" or answer == "Yes"):
                        done = True        
        else:
                answer = input("Wrong answer. Are you done?")    
                if(answer == "yes" or answer == "Yes"):
                        done = True      
print("Nice. You're final score was " + str(score))

maxLength = 0
maxWord = ""
for entry in boggleWords:
    if wordCheck(entry, Grid) and len(entry)>maxLength:
        maxWord = entry
        maxLength = len(entry)
        
print("The longest word was " + maxWord+".")

listOfWords.close()
            
                        
                        
                

#I've written and tested a function to find all close occurrences of a letter. Now I'll apply that function in a function to check whether a word is in the grid. 
                
            
            
            
    
