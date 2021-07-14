from utils import *


myfile = open("../../samples/easy.xml",'r')
text = [i.strip() for i in myfile.read().split("\n")]
Json = {}

# remove comments and unnecesary tags
modded = [tag for tag in text if not (tag.find("<?") == 0 or tag.find("<!") == 0)]

leafy(modded)
print(modded)





