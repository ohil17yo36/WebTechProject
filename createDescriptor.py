from lxml import etree
parser=etree.XMLParser(recover=True)
tree=etree.parse("sample.xml",parser=parser)
root=tree.getroot()
desList=[]
def height(root, depth):
	if root is None:
		return
	else:
		for child in root:
			#print child.attrib,depth
			desList.append(depth)
			height(child,depth+1)
		return

height(root,0)
for var in desList:
	print var