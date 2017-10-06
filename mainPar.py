############################################
#This is the one I really didn't finish!!!!#
############################################


wordCounter=1


f = open('paragraph_1.txt', 'r')
content=f.read()
wordContent=content.split(" ")
charContent=list(wordContent)
for word in wordContent:
	splitWord=word.split()
	#print(splitWord)
print("The number of words is: "+str(len(charContent))

f.close()