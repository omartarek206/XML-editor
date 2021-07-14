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


def leaf(node):
    """
    Check if node is a leaf, and print it
    """
    start = node.find(">")
    end = node.find("<", start)
    return (0,"") if end == -1 else (1, node[start+1:end])


def has_siblings(node,text):
    """
    Check if this node has any siblings
    """
    pass