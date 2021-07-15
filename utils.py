def leafy(text):
    """
    Remove newlines between the braces of a leaf
    """
    i = 0
    while True:
        if i < len(text):
            if text[i].find("<") ==-1:
                if i:
                    text[i] = text[i-1] + text[i] + text[i+1]
                    text.remove(text[i-1])
                    text.remove(text[i])
                else:
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


def areSiblings(text):
    """
    Check if this text is a set of siblings
    """
    openning = text[0]
    closing = "/" + text[0]
    end = text.index(closing)
    next = end+1
    if next<len(text):
        if text[next] == openning:
            return 1
    return 0
    

class str2(str):
    def __repr__(self):
        return ''.join(('"', super().__repr__()[1:-1], '"'))


def ignore(text):
    out1, out2 = [], []
    for tag in text:
        start = tag.find(" ")
        end = tag.find(">")
        new_tag = tag.replace(tag[start:end], "") if start != -1 else tag
        out1.append(new_tag)
    for tag in out1:
        start = tag.find("<!--")
        end = tag.find("-->") +3
        new_tag = tag.replace(tag[start:end], "") if start != -1 else tag
        out2.append(new_tag)
    return out2
    