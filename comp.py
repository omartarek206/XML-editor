def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
my_list=[]
s_det=[]
new_index=0
old_index=0
x={} 
x[' ']='s'
counter=2
f=open("compress_test.txt",'w') 
han=open("karim.txt",'r')
text=han.read()
splits = text.split()
for i   in splits:
    if i in x:
        f.write(x[i])
        f.write(x[' '])
    else:
        t=i
        x[t]=str(counter)
        f.write(x[t])
        f.write(x[' '])
        counter=counter+1

f.close()

key_list = list(x.keys())
val_list = list(x.values())
 
k=open("return.txt",'w') 

Z=open("compress_test.txt",'r')
rr=Z.read()
s_det=find(rr,'s')



r=open("compress_test.txt",'r')

count=0
for line in r:
    for i in range (len(line)):
        if count<len(s_det):
            """ if line[i]=='s':
                k.write(' ') """
            
            if count==0:
                    txt=line[0:s_det[count]]
                    count=count+1
                    my_list.append(txt)
            else:
                    txt=line[s_det[count-1]+1:s_det[count]]
                    count=count+1
                    my_list.append(txt) 

                
                
           
            
            
            
print("yes")
list_count=0



rr=open("compress_test.txt",'r')


for line in rr:
    for i in range (len(line)):
        if line[i]=='s':
            k.write(' ')
            
        else:
            if list_count<len(my_list):
                position = val_list.index(my_list[list_count])
                k.write(key_list[position])    
                list_count=list_count+1
       
k.close()        


    