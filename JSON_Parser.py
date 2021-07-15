import utils as u


myfile = open("../../samples/data-sample.xml",'r')
text = [i.strip() for i in myfile.read().split("\n")]
json = {}


# remove comments and unnecesary tags
modded = list(filter(u.notComment, text))
u.leafy(modded)

""" children = list(filter(u.isLeaf, modded))
print(children) """

""" parents = list(filter(u.notLeaf, modded))
print(parents) """
bare = list(map(u.strr, modded))
print(bare)

def jsonify(bare):
    # Output dict, openning and closing tags
    out = {}
    openning = bare[0]
    closing = "/" + bare[0]
    # Base case when at leaf
    if u.isLeaf(openning):
        for tag in bare:
            k,v = u.dictify(tag)
            out[k] = v
    # Perform recursive call otherwise
    else:
        # Check for the presense of siblings, and add them to a list
        outList = []
        if u.areSiblings(bare):
            i = 0
            keyTag = bare[0]
            while i < len(bare):
                start = bare[i:].index(bare[i]) + i + 1
                finish = bare[start:].index("/" + bare[i]) + start
                element = jsonify(bare[start:finish])
                outList.append(element)
                i = finish + 1
            out[keyTag] = outList
            return out
        child = bare[1:bare.index(closing)]
        out[openning] = jsonify(child)
    return out
        
json = jsonify(bare)
print(json)





        







