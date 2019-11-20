import os
from ParseDir import parseDir
from GetDictVizNode import getDictVizNode

testDirName = "0"
#用 getcwd以獲取腳本路徑而非套件路徑
currentPath = os.getcwd()
testPath = os.path.join(currentPath, testDirName)
testParse = parseDir(testPath)

testViz = getDictVizNode(testDirName, testParse)
#將目錄結構印成樹狀圖
testViz.visualize()
