import utils as u

def jsonify(bare):
    # Output dict, openning and closing tags
    out = {}
    outList = []
    openning = bare[0]
    closing = "/" + bare[0]
    # Base case when at leaf
    if u.isLeaf(openning):
        n = len(bare)-1     # Number of leafs -1
        keys = set()        # set of keys
        for tag in range(n):
            (k1,v1), (k2,v2) = u.dictify(bare[tag]), u.dictify(bare[tag+1])
            # Check for siblings
            if k2 == k1:
                keys.add(k1)
                outList.append(v1)
            else:
                if k1 in keys:
                    outList.append(v1)
                out[k1] = outList.copy() if outList else v1
                outList.clear()
                keys.clear()
            # Unrolled last iteration
            if n-1 == tag:
                if k2 == k1:
                    outList.append(v2)
                    out[k1] = outList
                else:
                    out[k2] = v2
                    outList.clear()
                keys.clear()
        
    # Perform recursive call otherwise
    else:
        # Check for the presense of siblings, and add them to a list
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