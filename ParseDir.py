import os

def parseDir(path):
    dirmap = {}
    dirNames = [name for name in os.listdir(path) if "." not in name]
    if len(dirNames) == 0:
        return dirmap
    else:
        for name in dirNames:
            dirPath = os.path.join(path, name)
            dirmap[name] = parseDir(dirPath)
        return dirmap
