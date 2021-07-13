def minify(path):
    return ''.join([i.strip() for i in open(path,'r').read().split("\n")])
