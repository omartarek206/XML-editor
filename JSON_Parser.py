import utils as u


myfile = open("../../samples/easy.xml",'r')
text = [i.strip() for i in myfile.read().split("\n")]
json = {}


# remove comments and unnecesary tags

modded = list(filter(u.notComment, text))

u.leafy(modded)

children = list(filter(u.isLeaf, modded))
print(children)
""" parents = list(filter(u.notLeaf, modded))
print(parents) """
bare = list(map(u.strr, modded))
print(bare)

def jsonify(bare):
    # Output dict, child list, openning and closing tags
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
        end = bare.index(closing)
        child = bare[1:end]
        out[openning] = jsonify(child)
    return out
        
json = jsonify(bare)
print(json)





        







