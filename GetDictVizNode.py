from treeviz.treeviz import Node

def getDictVizNode(name, child):
    root = Node(name)
    if len(child) == 0:
        return root
    else:
        for childName in child:
            childNode = getDictVizNode(childName, child[childName])
            root.add_child(childNode)
        return root
