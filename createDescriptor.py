from lxml import etree

parser=etree.XMLParser(recover=True)

tree1=etree.parse("sample2.html",parser=parser)
root1=tree1.getroot()
desList1=[]
#desList1.append(0)

tree2=etree.parse("sample.html",parser=parser)
root2=tree2.getroot()
desList2=[]
#desList2.append(0)

nodes1 = []
#nodes1.append(0)

nodes2 = []
#nodes2.append(0)

def height(root, depth, desList, nodes):
	if root is None:
		return
	else:
		nodes.append(root)
		desList.append(depth)
		for child in root:	
			height(child,depth+1, desList, nodes)
		return

height(root1, 1, desList1, nodes1)
height(root2, 1, desList2, nodes2)

print desList1
print desList2

if len(desList2)<len(desList1):
	desList1, desList2 = desList2, desList1
	nodes1, nodes2 = nodes2, nodes1

matchedTree1 = []
matchedTree2 = []

def compare(subTree):
	
	j = 0
	while j < len(desList2):
		
		dif = desList2[j] - subTree [0]
		i = 1
		p = j + 1
		if p >= len(desList2):
			break
		
		while i < len(subTree) and p < len(desList2):
			if desList2[p] - subTree[i] == dif:
				p = p + 1
				i = i + 1
				continue
			else:
				break

		if i == len(subTree):
			for k in range(j, p):
				desList2[k] = -1
			
			matchedTree2.append(j)

			return True
		j = j + 1

	return False

i = 0
j = 0
ans = 0

while i < len(desList1):
	j = i + 1
	subTree = []
	subTree.append(desList1[i])
	while j < len(desList1) and desList1[i] < desList1[j]:
		subTree.append(desList1[j])
		j = j + 1

	if j > i + 1 and compare(subTree): 
		ans = max(ans, len(subTree))
		matchedTree1.append(i)
		i = j
	else:
		i = i + 1

i = 0

print matchedTree1
print matchedTree2

if len(desList2)==1 or len(desList1)==1:
	print 1 
else:
	for i in range(len(matchedTree1)):
	    print nodes1[matchedTree1[i]].attrib, nodes1[matchedTree1[i]].tag
	    print nodes2[matchedTree2[i]].attrib, nodes2[matchedTree2[i]].tag

	print ans 

