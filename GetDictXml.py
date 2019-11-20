import xml.etree.cElementTree as ET

def getDictXml(name, child):
    root = ET.Element("dir", name=name)
    if len(child) == 0:
        return root
    else:
        for childName in child:
            childNode = getDictXml(childName, child[childName])
            root.append(childNode)
        return root
