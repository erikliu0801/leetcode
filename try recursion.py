#P112

#print(leafPath(List2TreeNode([5,10,20,15,25,30])))

#from Joseph
import os
def open_dir(root, valueList):
    for file in os.listdir(root):
        path = os.path.join(root, file)
        if os.path.isdir(path):
            valueList = open_dir(path, valueList)
        if file.split('.')[-1] == 'txt':
            valueList.append(file.split('.')[0])
    return valueList

valueList = []
valueList = open_dir('./root', valueList)
print(valueList)

#1.0
# ([5, 10, 15, 25, 20, 30], [[5, 10, 15, 25, 20, 30]])
def leafPath(root):
	leaf, leaf_s = [], []
	if root:
		leaf.append(root.val)
		leaf = leaf + leafPath(root.left)[0]
		leaf = leaf + leafPath(root.right)[0]	
		leaf_s.append(leaf)
	return leaf, leaf_s

#1.1
# 
def leafPath(root):
	leaf, leaf_s = [], []
	if root:
		leaf.append(root.val)
		for nums, nums_s in leafPath(root.left):
			leaf = leaf + nums
		leaf = leaf + leafPath(root.right)[0]	
		leaf_s.append(leaf)
	return leaf, leaf_s
#