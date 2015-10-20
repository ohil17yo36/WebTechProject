from lxml import etree

parser=etree.XMLParser(recover=True)

tree1=etree.parse("sample2.html",parser=parser)
root1=tree1.getroot()
desList1=[]

tree2=etree.parse("sample.html",parser=parser)
root2=tree2.getroot()
desList2=[]

nodes1 = []
nodes2 = []

diffarray1=[]
diffarray2=[]

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

#diffarray1[i] stores the difference between deslist1[i] and deslist1[i+1]
#diffarray2[i] stores the difference between deslist2[i] and deslist2[i+1]
for i in range(0,len(desList1)-1):
	diffarray1.append(desList1[i]-desList1[i+1])

for i in range(0,len(desList2)-1):
	diffarray2.append(desList2[i]-desList2[i+1])

if len(desList2)<len(desList1):
	desList1, desList2 = desList2, desList1
	nodes1, nodes2 = nodes2, nodes1
	diffarray1,diffarray2=diffarray2,diffarray1
	

matchedTree1 = []
matchedTree2 = []

# For knowing what the other variables like k,q,pi etc are please refer to Introduction to Algorithms by Cormen page number 1005 as its just too big to explain here :P
# Still here it goes pi[q] stores the longest length of prefix(denoted by k) of the pattern when the first q characters of the pattern match with the text
def kmpPreCompute(pattern):
	m=len(pattern)
	pattern=[0]+pattern	#I have implemented kmp on a 1 based index array. So initialy I am adding a value 0
	pi=[0,0] #I have implemented kmp on a 1 based index array. So initialy I am adding a value 0 and pi[1]=0
	k=0
	for q in range(2,m+1):
		while k>0 and pattern[k+1]!=pattern[q]:
			k=pi[k]
		if(pattern[k+1]==pattern[q]):
			k=k+1
		pi.append(k)	
	return pi

def kmp(pattern):
	global diffarray2
	n=len(diffarray2)
	m=len(pattern)
	pi=kmpPreCompute(pattern)
	diffarray2=[0]+diffarray2 #I have implemented kmp on a 1 based index array. So initialy I am adding a value 0
	pattern=[0]+pattern#I have implemented kmp on a 1 based index array. So initialy I am adding a value 0
	q=0
	for i in range(1,n+1):
		while q>0 and pattern[q+1]!=diffarray2[i]:
			q=pi[q]
		if pattern[q+1]==diffarray2[i]:
			q=q+1
		if q==m:
			diffarray2=diffarray2[1:i-m+1]+diffarray2[i+1:n+1] # The diffarray2 is spliced to exclude the part of the text that has been matched with the pattern.This is equivalent to replacing matched characters with -1.
			matchedTree2.append(i-m)#The start index of the text which matches the pattern
			return True
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

	if len(subTree)>1:
		pattern=diffarray1[i:j-1]# Our pattern diff array is stored in diffarray1[i:j-1]
		if kmp(pattern): 
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
##Bleh Code ends here	
