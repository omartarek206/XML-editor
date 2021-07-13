from stack import *
Tags=Stack()


han=open("karim.txt",'r')
flag=0

#looping on every char in every line in xml file
counter=0
for line in han:
    counter=counter+1
    for i in range (len(line)):
       
        #searching for <      
       if line[i]=='<':
           
           #searching for next char after < if not ! nor ? nor / 
           if line[i+1] !='?' and line[i+1] !='!'  :
               
               if line[i+1] !='/':
                    #searching for ' ' and > 
                    x=line.find(' ',i+1)
                    y=line.find('>',i+1)
                    if x==-1 :                   
                            tag=line[i+1:y]    
                            Tags.push(tag)   
                                     
                    else:
                            index=min(x,y)
                            tag=line[i+1:index]
                            Tags.push(tag)  
                                 
           
                   
                                  
               else:
                    
                    k=line.find('>',i+1)
                    closing=line[i+2:k]
                    if closing==Tags.peek():
                        Tags.pop()
                    else:
                        print("error in line: ",counter)
                        print("error detected in the following line: ")
                        print(line)  
                        
   
                


if Tags.isEmpty():
    print("xml is consistant")
else:  
    while Tags.isEmpty()==0:
        print(Tags.pop())
    print("xml isnot consistant")  