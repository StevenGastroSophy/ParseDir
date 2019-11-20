import os
import xml.etree.cElementTree as ET
from ParseDir import parseDir
from GetDictVizNode import getDictVizNode
from GetDictXml import getDictXml

testDirName = "0"
#用 getcwd以獲取腳本路徑而非套件路徑
currentPath = os.getcwd()
testPath = os.path.join(currentPath, testDirName)
testParse = parseDir(testPath)

#將目錄結構印成樹狀圖
testViz = getDictVizNode(testDirName, testParse)
testViz.visualize()

#產生 xml檔案
testXml = getDictXml(testDirName, testParse)
testXmlTree = ET.ElementTree(testXml)
testXmlTree.write("ParseDir.xml")
