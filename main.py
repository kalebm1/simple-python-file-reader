import sys
import io

charCount = 0
spaceCount = 0
wordCount = 0
symbolCount = 0

file = open('savage.txt')

while 1: 
      
    # read by character 
    char = file.read(1)           
    if not char:  
        break
          
    if char==" " or char=="\n" or char=="\t":
        wordCount+=1
        spaceCount+=1
    elif (char=="." or char=="?" or char=="," or char=="!" or char=="\"" or char=="\'" or char==":" or char=="(" or char==")" or char==";"):
        symbolCount+=1
    else:
        charCount+=1
    
print("Character Count = " + str(charCount))
print("Space Count = "+str(spaceCount))
print("Symbol Count = "+str(symbolCount))
print("Word Count = "+str(wordCount))
print("\n")
print("\n")
print("Average character count per word = "+str(charCount/wordCount))
print("\n")
print("\n")

file.close()