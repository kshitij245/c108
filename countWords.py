intro=input("enter your introduction")

#print(intro)
characterCount=0
wordCount=0
for i in intro:
    characterCount=characterCount+1
    #print(characterCount)
    if(i==" "):
        wordCount=wordCount+1
print("number of words")      
print(wordCount) 

print("number of character")
print(characterCount)
    
