import utils as u
from jsonify import *

def xml_to_dict(rPath):
    myfile = open(rPath,'r')
    text = [i.strip() for i in myfile.read().split("\n")]

    # Remove comments and unnecesary tags
    modded = list(filter(u.notComment, text))
    
    # Remove unnecssary new lines
    u.leafy(modded)

    # Remove tags
    bare = list(map(u.strr, modded))
  
    return jsonify(bare)
    
def dict_to_json(wPath, dicto):
    fileWrite = open(wPath, 'w')
    print(dicto, file=fileWrite)


path_read = "E:\Study\DS Project\Samples\easy.xml"
mydict = xml_to_dict(path_read)
path_write = "E:\Study\DS Project\Samples\jsonify-program-temporary-cache.json"
dict_to_json(path_write, mydict)

            







