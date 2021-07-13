from stack import *
def error_checking(path):
    Tags=Stack()
    mylist=[]


    han=open(path,'r')
    flag=0
    text = [i.strip() for i in han.read().split("\n")]


    #looping on every char in every line in xml file
    counter=0
    for line in text:
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

                        if line[y-1]=='/':
                            continue
                        if x==-1 :              
                                ind=str(counter)
                                tag=line[i+1:y]+' '+ind                             
                                Tags.push(tag)   
                                        
                        else:
                                ind=str(counter)
                                index=min(x,y)                      
                                tag=line[i+1:index]+' '+ind
                                Tags.push(tag)  
                                    
            
                    
                                    
                else:
                        
                        k=line.find('>',i+1)
                        closing=line[i+2:k]
                        n=Tags.peek()
                        m=n.find(' ')
                        b=n[:m]
                        

                        if closing==b:
                            Tags.pop()
                        else:
                            q=Tags.pop()
                            t=q.find(' ')
                            err_line=q[t:]
                            mylist.append(err_line)
                            flag=1                    

                            
                               
    if flag==0:
        con_or_not=0
        if Tags.isEmpty():
            con_or_not=1
        else:  
            pass 

    if flag==1:
        return 1,mylist
    elif flag==0 and con_or_not==1:
        return 0,mylist
    else:
        return 1,mylist     
    

path="karim.txt"
x,y=error_checking(path)

if x==1:
    if len(y)==0:
         print("xml isnot consistant") 
         print("error due to not closing tags")
    else:
         print("xml isnot consistant") 
         for x in range(len(y)):
             print("error in following line:",y[x])
             
else:
    print("xml is consistant")        