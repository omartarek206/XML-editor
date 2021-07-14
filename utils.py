def leafy(text):
    """
    Remove newlines between the braces of a leaf
    """
    i = 0
    while True:
        if i < len(text):
            if text[i].find("<") ==-1:
                text[i] = text[i-1] + text[i] + text[i+1]
                text.remove(text[i-1])
                text.remove(text[i])
            i+=1
        else:
            break


def isLeaf(tag):
    """
    Check if tag is a leaf
    """
    return 0 if tag.find("<", tag.find(">")) == -1 else 1


def notLeaf(tag):
    """
    Check if tag is not a leaf
    """
    return isLeaf(tag) ^ 1


def notComment(tag):
    """
    Return false if tag is a comment
    """
    return 1 if not (tag.find("<?") == 0 or tag.find("<!") == 0) else 0


def strr(tag):
    """
    Return tag without braces
    """
    return tag[1:-1] if notLeaf(tag) else tag


def dictify(tag):
    """
    Convert tag into key value tuple
    """
    return tag[tag.find('<')+1 : tag.find('>')], tag[tag.find('>')+1 : tag.find("</")]


def hasSiblings(tag,text):
    """
    Check if this tag has any siblings
    """
    