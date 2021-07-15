x={} 


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def compress(path):
    compressed_file=""
    s_det=[]
   
    x[' ']='s'
    counter=2
    

    han=open(path,'r')
    text=han.read()
    splits = text.split()
    for i   in splits:
        if i in x:
            compressed_file=compressed_file+x[i]+x[' ']
        else:
            t=i
            x[t]=str(counter)
            compressed_file=compressed_file+x[t]+x[' ']
            counter=counter+1

    return compressed_file        



def decompress(path):
    
    my_list=[]
    decompressed_file=""

    key_list = list(x.keys())
    val_list = list(x.values())
    


    Z=open(path,'r')
    rr=Z.read()

    s_det=find(rr,'s')



    r=open(path,'r') 
    

    count=0

    for line in r:
        for i in range (len(line)):
            if count<len(s_det):        
                if count==0:
                    txt=line[0:s_det[count]]
                    count=count+1
                    my_list.append(txt)
                    
                            
                else:
                
                    txt=line[s_det[count-1]+1:s_det[count]]
                    
                    count=count+1
                    my_list.append(txt) 

    list_count=0



    kk=open(path,'r')    
    for line in kk:
        for i in range (len(line)):
            if line[i]=='s':
                decompressed_file=decompressed_file+' '
                
                
            else:
                if list_count<len(my_list):
                    position = val_list.index(my_list[list_count])
                    decompressed_file=decompressed_file+key_list[position]
                    list_count=list_count+1
                        
    return(decompressed_file)

