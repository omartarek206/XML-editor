from stack import *
Tags=Stack()


han=open("karim.txt",'r')

#looping on every char in every line in xml file

for line in han:
    for i in range (len(line)):
        #searching for <
       if line[i]=='<':
           #searching for next char after < if not ! nor ? nor / 
           if line[i+1] !='?' and line[i+1] !='!' and line[i+1] !='/':
               #searching for ' ' and > 
               x=line.find(' ',i+1)
               y=line.find('>')
               if x==-1 :
                   
                    tag=line[1:y]    
                    Tags.push(tag)             
               else:
                    tag=line[i+1:x]
                    Tags.push(tag)
                    


print(Tags.pop())

print(Tags.pop())

