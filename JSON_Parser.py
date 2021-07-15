import utils as u
from jsonify import *


def xml_to_dict(rPath):
    myfile = open(rPath,'r')
    text = [u.str2(i.strip()) for i in myfile.read().split("\n")]

    # Remove comments and unnecesary tags
    modded = list(filter(u.notComment, text))
    
    # Remove unnecssary new lines
    u.leafy(modded)

    # Ignore attributes
    final = u.ignore(modded)

    # Remove tags
    bare = list(map(u.strr, final))
  
    return jsonify(bare)
    
def dict_to_json(wPath, dicto):
    fileWrite = open(wPath, 'w')
    print(dicto, file=fileWrite)

            







