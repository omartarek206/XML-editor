

def prettify (path):
    rread = open(path, 'r+')
    #to open read file


    spaces = 0
    #intialize number of spaces with zero
    prev = "3amour"
    #string variable to check for open and close tags
    s = ""
    #the string to be returned


    for line in rread:

        line=line.lstrip()
        #to make sure that all text shifted left



        i = line.find('<')
        j = line.find('>')
        k = line.find('/')


        l = line.find("<?",0,3)
        m=line.find("<!",0,3)
        #check for comments to be not shifted

        o=line.find("<data version=")
        # check for data version to be not shifted





        if l!=-1 or m!=-1 :
            prev = "open"
        if o!=-1:
            prev = "open"
        if i!=-1 and j!=-1 and l == -1 and m == -1 and o == -1:

            if k != -1 and line[k-1] == '<':
                if line[i + 1] != '/' and line[k+1] !='>':
                    if prev == "open":
                        spaces += 4
                    prev = "close"
                else:
                    if prev == "close":
                        spaces -= 4
                    prev = "close"
            if k == -1:
                if prev == "open":
                    spaces += 4
                prev = "open"

            if k != -1 and line[k - 1] != '<' and line[k+1] !='>':
                if prev == "open":
                    spaces+=4
                prev = "open"


        for x in range(spaces):
            s += ' '
        s += line

    return s






































