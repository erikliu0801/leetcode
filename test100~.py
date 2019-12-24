#100
def isSameTree(p, q):
	def levelOrderTraversal(TreeNode):
		"""
		rtype: left_list, right_list
		highest_treenode belongs to left_list
		"""
		level_order_treenode_left = [TreeNode]
		level_order_treenode_right = []
		m, n, last_len = 0, 0, 0
		while last_len != len(level_order_treenode_left + level_order_treenode_right):
			last_len, l, r = len(level_order_treenode_left + level_order_treenode_right), m, n
			level_order_treenode = level_order_treenode_left[m:] + level_order_treenode_right[n:]
			for i in range(len(level_order_treenode)):
				if level_order_treenode[i].left != None:
					level_order_treenode_left.append(level_order_treenode[i].left)
				else:
					level_order_treenode_left.append(None)
				if level_order_treenode[i].right != None:
					level_order_treenode_right.append(level_order_treenode[i].right)
				else:
					level_order_treenode_right.append(None)
				if level_order_treenode[i] in level_order_treenode_left:
					m += 1
				else:
					n += 1
		return level_order_treenode_left, level_order_treenode_right

	if p is None or q is None:
		if p is None and q is None:
			return True
		else:
			return False
	else:
		p_list_left, p_list_right = levelOrderTraversal(p)
		q_list_left, q_list_right = levelOrderTraversal(q)
		if len(p_list_left) != len(q_list_left) or len(p_list_right) != len(q_list_right):
			return False
		p_list, q_list = p_list_left + p_list_right, q_list_left + q_list_right
		for i in range(len(p_list)):
			if p_list[i].val != q_list[i].val:
				return False
		return True

#101
def isSymmetric(root):
	def mirrorTree(tree_node):
		if type(tree_node) != TreeNode:
			return 
		else:
			checked_treenode = 0
			treenode_list = [tree_node]
			while checked_treenode != len(treenode_list):
				level_treenode = treenode_list[checked_treenode:]
				for node in level_treenode:
					if node != None:
						if node.left == None and node.right == None:
							pass
						elif node.left != None or node.right != None:
							_ = node.left
							node.left, node.right = node.right, _
							if node.left != None:
								treenode_list.append(node.left)
							if node.right != None:
								treenode_list.append(node.right)
					checked_treenode += 1
			return tree_node
	def TreeNode2List(tree_node):
		if type(tree_node) != TreeNode:
			return []
		else:
			checked_treenode = 0
			treenode_list = [tree_node]
			while checked_treenode != len(treenode_list):
				level_treenode = treenode_list[checked_treenode:]
				for treenode in level_treenode:
					if treenode != None:
						if treenode.left != None:
							treenode_list.append(treenode.left)
						else:
							treenode_list.append(None)
						if treenode.right != None:
							treenode_list.append(treenode.right)
						else:
							treenode_list.append(None)
					checked_treenode += 1
			for _ in range(len(treenode_list)):
				if treenode_list[-1] == None:
					treenode_list.pop(-1)
				else:
					break
			for i in range(len(treenode_list)):
				if treenode_list[i] != None:
					treenode_list[i] = treenode_list[i].val
			return treenode_list
	original_list = TreeNode2List(root)
	mirror_tree = mirrorTree(root)
	if not mirror_tree:
		return True
	else:
		if original_list == TreeNode2List(mirror_tree):
			return True
		else:
			return False

#104
def maxDepth(root):
	if type(root) != TreeNode:
		return 0
	else:
		checked_treenode, depth = 0, 0
		treenode_list = [root]
		while checked_treenode != len(treenode_list):
			alive_node = len(treenode_list)
			level_treenode = treenode_list[checked_treenode:]			
			for node in level_treenode:
				if node != None:
					if node.left != None:
						treenode_list.append(node.left)
					else:
						treenode_list.append(None)
					if node.right != None:
						treenode_list.append(node.right)
					else:
						treenode_list.append(None)
				checked_treenode += 1
			if len(treenode_list) > alive_node:
				depth += 1
		return depth

#107
def levelOrderBottom(root):
	if type(root) != TreeNode:
		return []
	else:
		checked_treenode, k, dead_num = 0, 0, 0
		treenode_list, level_nums= [root], []
		while checked_treenode != len(treenode_list):
			level_treenode = treenode_list[checked_treenode:]
			level_nums.append(len(level_treenode)-dead_num)
			dead_num = 0
			for treenode in level_treenode:
				if treenode != None:
					if treenode.left != None:
						treenode_list.append(treenode.left)
					else:
						treenode_list.append(None)
						dead_num += 1
					if treenode.right != None:
						treenode_list.append(treenode.right)
					else:
						treenode_list.append(None)
						dead_num += 1
				checked_treenode += 1			
			k += 1
		#
		for _ in range(len(level_nums)):
			if level_nums[-1] == 0:
				level_nums.pop(-1)
			else:
				break
		#
		while treenode_list.count(None) != 0:
			treenode_list.remove(None)
		for i in range(len(level_nums)):
			level_val=[]
			for _ in range(level_nums[i]):
				level_val.append(treenode_list[0].val)
				treenode_list.pop(0)
			level_nums[i] = level_val
		# list.reverse() not work
		answer = []
		for i in range(1, len(level_nums)+1):
			answer.append(level_nums[-i])
		return answer

#108
def sortedArrayToBST(nums):
	if len(nums)==0:
		return
	else:
		medium = len(nums)//2
		root = TreeNode(nums[medium])
		tree_left = nums[:medium] #exclude root
		tree_left.reverse() #tree_left = nums[:medium+1].reverse() will return None
		tree_right = nums[medium+1:] #exclude root
		tree_left.insert(0, root) #include root
		tree_right.insert(0, root) #include root
		for i in range(len(tree_left)-1):
			tree_left[i].left = TreeNode(tree_left[i+1])
			tree_left[i+1] = tree_left[i].left
		for i in range(len(tree_right)-1):
			tree_right[i].right = TreeNode(tree_right[i+1])
			tree_right[i + 1] = tree_right[i].right
		return root

#110
def isBalanced(root):
	pass

#111
def minDepth(root):
	if type(root) != TreeNode:
		return 0
	else:
		checked_treenode, depth, leaf_end = 0, 0, False
		treenode_list = [root]
		while leaf_end != True:
			alive_node = len(treenode_list)
			level_treenode = treenode_list[checked_treenode:]
			for node in level_treenode:
				if node != None:
					if node.left == None and node.right == None:
						leaf_end = True
						break
					if node.left != None:
						treenode_list.append(node.left)
					else:
						treenode_list.append(None)
					if node.right != None:
						treenode_list.append(node.right)
					else:
						treenode_list.append(None)
				checked_treenode += 1
			depth += 1
		return depth

#112
def hasPathSum(root, sum):
	def leafPath(root):			
		leaf_s, leaf_s_val = [], []
		if root:
			leaf_s_left, leaf_s_val_left = leafPath(root.left)
			leaf_s_right, leaf_s_val_right = leafPath(root.right)
			leaf_s, leaf_s_val = leaf_s + leaf_s_left + leaf_s_right, leaf_s_val + leaf_s_val_left + leaf_s_val_right
			if root.left == None and root.right == None:
				leaf_s.append([root])
				leaf_s_val.append([root.val])
			for i, leaf in enumerate(leaf_s):
				if root.left in leaf or root.right in leaf:
					leaf_s[i].insert(0,root)
					leaf_s_val[i].insert(0,root.val)
		return leaf_s, leaf_s_val
	def leafPathSum(leaf_s_val):		
		for i, leaf in enumerate(leaf_s_val):
			leaf_sum = 0
			for val in leaf:
				leaf_sum += val
			leaf_s_val[i] = leaf_sum
		return leaf_s_val
	_, leaf_s_val = leafPath(root)
	leaf_sum = leafPathSum(leaf_s_val)
	if sum in leaf_sum:
		return True
	else:
		return False















if __name__ == '__main__':
	class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

	def List2TreeNode(nums):
		"""
		nums: List
		rtype: highest TreeNode
		"""
		if len(nums)==0:
			return
		else:
			alive_node, checked_num = 0, 1 #int: by level
			treenode = [TreeNode(nums[0])]
			while alive_node != len(treenode):
				level_treenode = treenode[alive_node:] #list
				if checked_num <= len(nums):
					rest_nums = nums[checked_num:]
				else:
					break
				for i in range(len(level_treenode)):			
					if i*2 <= len(rest_nums) -1 :
						if rest_nums[i*2] != None:
							treenode[alive_node].left = TreeNode(rest_nums[i*2])
							treenode.append(treenode[alive_node].left)
					if i*2 <= len(rest_nums) -2 :
						if rest_nums[i*2+1] != None:
							treenode[alive_node].right = TreeNode(rest_nums[i*2+1])
							treenode.append(treenode[alive_node].right)
					checked_num += 2
					alive_node += 1
			return treenode[0]

	def TreeNode2List(tree_node):
		if type(tree_node) != TreeNode:
			return []
		else:
			checked_treenode = 0
			treenode_list = [tree_node]
			while checked_treenode != len(treenode_list):
				level_treenode = treenode_list[checked_treenode:]
				for treenode in level_treenode:
					if treenode != None:
						if treenode.left != None:
							treenode_list.append(treenode.left)
						else:
							treenode_list.append(None)
						if treenode.right != None:
							treenode_list.append(treenode.right)
						else:
							treenode_list.append(None)
					checked_treenode += 1
			for _ in range(len(treenode_list)):
				if treenode_list[-1] == None:
					treenode_list.pop(-1)
				else:
					break
			for i in range(len(treenode_list)):
				if treenode_list[i] != None:
					treenode_list[i] = treenode_list[i].val
			return treenode_list

	#100
	# input_p_list = [
	# [1,2],
	# [],
	# [10,5,15],
	# [2, None, 4],
	# [0],
	# [1,None,2,3],
	# [390,255,2266,-273,337,1105,3440,-425,4113,None,None,600,1355,3241,4731,-488,-367,16,None,565,780,1311,1755,3075,3392,4725,4817,None,None,None,None,-187,152,395,None,728,977,1270,None,1611,1786,2991,3175,3286,None,164,None,None,4864,-252,-95,82,None,391,469,638,769,862,1045,1138,None,1460,1663,None,1838,2891,None,None,None,None,3296,3670,4381,None,4905,None,None,None,-58,None,None,None,None,None,None,None,None,734,None,843,958,None,None,None,1163,1445,1533,None,None,None,2111,2792,None,None,None,3493,3933,4302,4488,None,None,None,None,None,None,819,None,None,None,None,1216,None,None,1522,None,1889,2238,2558,2832,None,3519,3848,4090,4165,None,4404,4630,None,None,None,None,None,None,1885,2018,2199,None,2364,2678,None,None,None,3618,3751,None,4006,None,None,4246,None,None,4554,None,None,None,1936,None,None,None,None,2444,2642,2732,None,None,None,None,None,None,None,4253,None,None,None,None,2393,2461,None,None,None,None,4250,None,None,None,None,2537]]
	# input_q_list = [
	# [1,None,2],
	# [],
	# [10,5,None,None,15],
	# [2,3,4],
	# [0],
	# [1,None,2,None,3],
	# [390,255,2266,-273,337,1105,3440,-425,4113,None,None,600,1355,3241,4731,-488,-367,16,None,565,780,1311,1755,3075,3392,4725,4817,None,None,None,None,-187,152,395,None,728,977,1270,None,1611,1786,2991,3175,3286,None,164,None,None,4864,-252,-95,82,None,391,469,638,769,862,1045,1138,None,1460,1663,None,1838,2891,None,None,None,None,3296,3670,4381,None,4905,None,None,None,-58,None,None,None,None,None,None,None,None,734,None,843,958,None,None,None,1163,1445,1533,None,None,None,2111,2792,None,None,None,3493,3933,4302,4488,None,None,None,None,None,None,819,None,None,None,None,1216,None,None,1522,None,1889,2238,2558,2832,None,3519,3848,4090,4165,None,4404,4630,None,None,None,None,None,None,1885,2018,2199,None,2364,2678,None,None,None,3618,3751,None,4006,None,None,4246,None,None,4554,None,None,None,1936,None,None,None,None,2444,2642,2732,None,None,None,None,None,None,None,4253,None,None,None,None,2461,2393,None,None,None,None,4250,None,None,None,None,2537]]
	# expected_output = [False, True, False, False, True, False, False]
	
	# for i in range(len(input_p_list)):
	# 	print(List2TreeNode(input_p_list[i]))

	# print(TreeNode2List(List2TreeNode([10,5,None,None,15,1])))

	# for i in range(len(input_p_list)):
	# 	if isSameTree(List2TreeNode(input_p_list[i]), List2TreeNode(input_q_list[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(TreeNode2List(isSameTree(List2TreeNode(input_p_list[i]), List2TreeNode(input_q_list[i]))))
	# 	else:
	# 		print("Right")

	# print(isSameTree(List2TreeNode(input_p_list[-1]), List2TreeNode(input_q_list[-1])))

	#101
	# input_treenode = [
	# [1,2,7,3,4,4,3],
	# [1,2,2,None,3,3],
	# [1,2,2,None,3,None,3]]
	# expected_output = [True, True, False]
	# for i in range(len(input_treenode)):
	# 	if isSymmetric(List2TreeNode(input_treenode[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(isSymmetric(List2TreeNode(input_treenode[i])))
	# 	else:
	# 		print("Right")
	# print(isSymmetric(List2TreeNode(input_treenode[-1])))

	#104
	# input_nums = [[3,9,20,None,None,15,7]]
	# expected_output = [3]
	# for i in range(len(input_nums)):
	# 	if maxDepth(List2TreeNode(input_nums[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(maxDepth(List2TreeNode(input_nums[i])))
	# 	else:
	# 		print("Right")		
	# print(maxDepth(List2TreeNode(input_nums[-1])))

	#107
	# input_nums = [[3,9,20,None,None,15,7]]
	# expected_output = [[[15,7],[9,20],[3]]]
	# for i in range(len(input_nums)):
	# 	if levelOrderBottom(List2TreeNode(input_nums[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(levelOrderBottom(List2TreeNode(input_nums[i])))
	# 	else:
	# 		print("Right")
	# print(levelOrderBottom(List2TreeNode(input_nums[-1])))
	
	#108
	# input_nums = [[-10, -3, 0, 5, 9]]
	# expected_output = []
	# for i in range(len(input_nums)):
	# 	if sortedArrayToBST(input_nums[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(sortedArrayToBST(input_nums[i]))
	# 	else:
	# 		print("Right")
	# print(sortedArrayToBST(input_nums[-1]))

	#110

	#111
	# Left -> Root -> Right
	def inOrderTraversal(root):
		res = []
		if root:
			res = inOrderTraversal(root.left)
			res.append(root.val)
			res = res + inOrderTraversal(root.right)
		return res

	# Root -> Left ->Right
	def preOrderTraversal(root):
		res = []
		if root:
			res.append(root.val)
			res = res + preOrderTraversal(root.left) #return two val
			res = res + preOrderTraversal(root.right)
		return res

	# Left ->Right -> Root
	def postOrderTraversal(root):
		res = []
		if root:
			res = postOrderTraversal(root.left)
			res = res + postOrderTraversal(root.right)
			res.append(root.val)
		return res

	# print(inOrderTraversal(List2TreeNode([5,10,20,15,25,30])))
	# print(preOrderTraversal(List2TreeNode([5,10,20,15,25,30])))
	# print(postOrderTraversal(List2TreeNode([5,10,20,15,25,30])))

	#112
	input_root = [[-790,-726,970,696,-266,-545,830,-866,669,-488,-122,260,116,521,-866,-480,-573,-926,88,733,None,None,483,-935,-285,-258,892,180,279,-935,675,2,596,5,50,830,-607,-212,663,25,-840,None,None,-333,754,None,817,842,-220,-269,9,-862,-78,-473,643,536,-142,773,485,262,360,702,-661,244,-96,None,519,566,-893,-599,126,-314,160,358,159,None,None,-237,-522,-327,310,-506,462,-705,868,-782,300,-945,-3,139,-193,-205,-92,795,-99,-983,-658,-114,-706,987,292,None,234,-406,-993,-863,859,875,383,-729,-748,-258,329,431,-188,-375,-696,-856,825,-154,-398,-917,-70,105,819,-264,993,207,21,-102,50,569,-824,-604,895,-564,-361,110,-965,-11,557,None,202,213,-141,759,214,207,135,329,15,None,None,244,None,334,628,509,627,-737,-33,-339,-985,349,267,-505,-527,882,-352,-357,-630,782,-215,-555,132,-835,-421,751,0,-792,-575,-615,-690,718,248,882,-606,-53,157,750,862,None,940,160,47,-347,-101,-947,739,894,None,-658,-90,-277,-925,997,862,-481,-83,708,706,686,-542,485,517,-922,978,-464,-923,710,-691,168,-607,-888,-439,499,794,-601,435,-114,-337,422,None,-855,-859,163,-224,902,None,577,None,-386,272,-971,-137,671,-410,-529,733,-956,-371,-676,-292,None,None,-606,617,431,-609,-429,-509,None,138,363,None,None,None,548,-672,324,-161,-463,-217,644,-480,535,-324,-32,-386,799,652,102,-339,294,None,None,None,948,733,None,118,388,-195,-144,424,447,-563,None,None,None,None,591,32,438,260,-826,-463,-201,-944,-195,3,617,257,-252,-865,552,304,-445,-416,886,-665,-417,527,105,-373,520,-379,844,403,300,-450,981,400,-633,858,-69,314,133,-764,-263,-624,-758,-685,-799,-860,859,-659,-616,129,-788,362,-209,559,246,-27,-193,None,None,114,872,622,34,766,None,333,677,None,-104,-429,923,-563,None,630,754,735,815,931,364,306,933,786,-156,-265,453,-738,837,-983,-357,818,9,-243,921,-411,-813,-901,677,-544,866,-816,819,379,217,None,None,-97,None,30,-765,None,None,None,None,None,None,484,-815,-416,-260,-704,-774,-369,-875,None,None,None,None,82,-546,-565,23,None,-156,None,816,168,-398,-264,None,161,-83,-422,-499,-215,-689,-887,-495,2,-281,-2,None,881,None,None,-897,-194,-852,297,-879,569,-501,982,725,850,None,161,-530,-417,-252,-147,-215,-561,-373,-356,344,-883,274,308,-261,-271,-520,-48,None,484,None,None,None,421,151,870,-979,660,-65,962,None,-338,182,655,736,-340,-122,201,-424,-473,None,401,-887,282,None,None,-290,814,-874,337,-834,675,-495,506,-739,-427,None,None,913,887,604,None,808,658,None,None,-677,758,-591,-805,361,None,163,-308,276,-946,None,981,-949,318,392,-876,-173,-739,698,-968,None,858,-666,983,-600,-701,-337,None,-884,885,-737,-843,-62,-694,None,None,None,None,None,145,354,-116,-711,-116,587,589,269,None,-422,None,224,-520,None,None,237,-779,890,-82,None,None,-524,-532,None,-685,144,-672,452,-134,930,330,None,None,295,-997,7,787,373,-236,476,880,-661,-601,None,None,-618,None,None,81,-703,-109,-643,705,-62,-30,-765,466,664,-120,46,440,122,766,-336,-542,-420,-349,111,None,None,-445,-619,-903,120,364,-139,None,-708,759,-82,232,639,-500,582,942,335,-863,None,956,944,-383,-219,257,-276,-199,231,790,113,None,43,None,-840,None,902,-445,876,956,-357,-599,51,None,841,-465,-568,712,-724,886,None,64,840,-184,-783,567,-908,954,None,16,592,-396,-666,-150,366,143,-493,None,-298,-476,495,None,-454,292,895,9,379,None,None,290,-890,-165,-722,949,-720,810,879,-343,-683,-84,343,-38,-163,101,None,506,None,None,None,None,None,None,None,150,None,-433,None,-367,907,-311,-379,-829,-845,616,-871,None,None,None,None,None,None,None,-886,None,None,-494,301,263,-795,None,976,581,-850,850,-882,159,188,76,None,None,-426,-573,529,-149,941,-999,-774,None,-987,None,None,925,None,None,407,-666,-620,430,841,None,-152,900,-67,-704,749,226,869,-580,595,-732,None,58,65,-322,-312,-133,168,104,114,-846,368,-307,-669,None,-670,-949,262,47,None,175,841,None,-241,-49,797,-300,-967,-514,90,79,-558,-933,660,None,-883,47,-532,-962,None,-630,545,274,-295,-137,None,None,-91,633,None,-248,None,27,None,None,-223,-262,979,-931,None,None,None,-261,None,915,-468,None,-565,463,236,None,788,-522,496,-542,223,473,348,-952,None,620,915,593,None,None,None,918,319,None,446,868,-636,325,-781,-667,578,-462,614,None,-260,None,116,None,562,-510,-244,-905,131,350,None,None,840,-158,536,None,34,-701,-281,56,174,-605,752,868,-71,-327,-792,-511,None,-194,267,-454,-280,836,None,973,None,513,677,None,182,93,-985,73,-279,617,None,906,-173,None,21,844,None,-383,-833,761,216,-172,None,346,304,None,-703,None,-195,928,893,-588,-1,-504,272,-335,-233,None,None,None,518,-653,817,None,797,493,718,None,None,-913,-36,None,-833,None,606,None,-914,-996,None,None,-132,None,93,None,None,None,None,None,None,438,None,None,196,None,None,-745,None,890,None,None,403,None,None,134,None,None,682,-728,None,None,-808,None,-829,-124,253,934,647,-780,460,600,631,-429,-136,994,847,None,-50,388,None,None,None,None,None,881,901,None,None,-691,347,-435,-204,-274,237,568,None,-689,-84,942,-411,725,-475,315,-688,-405,-815,-644,926,-990,-470,-354,781,517,-831,-152,-335,397,282,-289,83,-981,None,None,738,0,300,None,209,None,313,797,212,146,590,-430,804,None,None,395,590,23,None,None,None,None,-604,None,None,None,559,656,None,None,974,-561,None,4,80,-935,None,284,-353,None,None,-367,-714,None,-915,-402,None,691,48,-836,None,754,2,-99,86,-385,-662,70,172,-889,-370,None,932,273,465,196,None,813,-327,-64,349,531,983,919,-27,-196,637,-384,-594,-796,None,None,-617,None,161,654,63,565,660,233,-33,None,-637,None,None,None,None,None,757,-65,400,267,-561,None,219,-927,-143,-813,-417,-637,-22,101,-809,938,None,177,None,None,233,None,63,None,-665,53,808,-803,-397,None,-309,-446,-384,731,-85,None,-74,-133,-282,-489,-581,None,None,-950,291,-942,77,None,373,170,-849,261,None,-583,-339,707,None,58,None,None,None,None,-994,None,-519,None,-858,None,None,None,-348,-229,738,713,None,None,None,None,None,-585,None,-206,None,None,770,None,None,-292,None,886,-109,None,None,None,748,-328,-146,-329,-299,-927,-381,-77,74,441,None,None,881,-37,None,930,None,None,None,None,None,-155,-717,-595,None,442,None,-891,241,-978,-503,213,668,None,773,None,None,None,-48,-291,-587,318,954,-972,461,825,390,-618,984,-988,None,None,-91,808,664,-451,-911,-343,-421,-131,653,None,478,791,420,848,383,None,None,None,-583,444,-512,509,436,-284,500,175,540,837,None,None,None,None,-695,-337,None,50,None,None,None,None,-173,None,None,None,None,None,None,None,-826,-734,-731,612,-396,None,None,545,-631,618,-713,413,-239,-191,164,-595,None,None,-845,364,727,-689,922,909,None,None,-445,9,532,-502,None,None,-37,388,None,130,None,164,-836,None,None,-798,None,None,-610,145,-360,-683,491,-857,None,-834,None,664,-918,-369,None,-556,263,-85,674,None,None,None,782,-886,-430,-362,-630,None,-408,108,647,-985,949,-82,-182,None,-119,-72,None,-322,None,125,None,None,None,None,None,None,-656,-125,675,671,None,620,-124,297,-912,None,None,None,None,None,597,265,None,606,-262,-298,-324,None,None,None,-910,-534,None,None,-604,-584,-775,180,-840,495,None,None,537,-372,306,77,553,603,None,None,472,362,None,307,272,None,-75,760,None,None,-961,-540,536,None,-1,None,518,-869,None,None,None,885,-971,-936,-320,174,291,259,-918,None,None,None,-144,-786,962,-105,939,None,None,None,-313,789,None,-304,None,None,None,-799,None,None,None,None,292,-910,None,None,None,None,857,-128,-128,90,422,896,726,None,None,None,None,None,None,None,902,None,None,-457,-958,None,-324,-364,None,-801,78,None,None,None,473,None,None,50,-224,-314,-137,652,338,None,None,-184,969,None,None,None,None,None,-413,-147,None,None,None,None,None,338,-274,None,-265,None,-421,None,89,-344,None,None,None,None,None,None,-102,843,None,None,-60,824,-584,None,None,None,167,-776,545,147,-353,-68,188,832,-394,535,907,None,914,-165,-621,None,None,None,793,None,None,-523,-493,None,-15,20,425,-320,-63,67,None,None,-887,458,-906,None,617,None,None,None,-722,None,None,-332,191,501,713,-862,None,None,-400,-88,105,535,723,-545,None,405,None,None,-301,-832,-379,445,-990,911,-433,-438,-808,-98,631,532,None,-417,-179,302,-605,308,680,-493,-22,764,815,-443,193,-542,247,12,-104,509,-993,-110,None,569,None,None,-726,None,None,None,None,-998,258,None,914,341,-858,None,None,None,87,-586,None,None,-567,44,263,862,None,None,831,121,None,None,None,596,873,None,-689,None,-80,917,None,-299,810,None,636,-917,414,-501,801,448,None,None,977,None,268,None,-704,None,None,696,-568,-234,None,-559,446,909,-101,608,None,None,None,57,None,689,706,-524,174,856,None,None,-768,290,395,-845,None,None,None,None,-189,-526,None,-734,None,860,750,-579,251,-969,544,None,725,-18,None,-56,None,None,511,-646,431,612,None,-174,471,-903,None,995,None,758,767,907,-516,-264,-672,-94,None,None,460,-376,None,None,-301,-910,928,-281,None,None,-466,None,-74,154,None,599,None,None,346,None,-522,-458,-644,306,-505,None,-672,746,511,None,-627,None,772,None,None,-924,-805,-182,921,256,169,-970,-911,-301,None,736,None,None,None,-616,-923,-104,395,-252,583,382,179,-336,-956,-249,None,263,160,None,None,None,None,None,-442,-340,-118,888,None,-840,-597,-202,675,727,27,-530,146,None,None,None,670,619,None,None,98,987,163,None,339,None,None,208,None,None,769,-998,None,403,None,None,None,None,None,-444,None,None,None,234,-642,None,None,None,None,468,None,None,None,None,None,-972,None,None,None,None,None,None,None,360,-101,-243,None,None,748,None,415,-853,-81,-480,608,-689,816,353,572,-596,671,-108,None,None,-239,None,None,None,-67,301,311,None,-727,None,-70,None,-657,None,None,None,266,-998,-725,973,371,262,None,None,None,380,-583,None,None,-609,259,-704,-117,None,-996,-131,None,-737,111,None,777,398,637,538,656,714,None,773,None,461,392,None,None,None,-88,None,977,943,-335,-587,-702,848,391,968,None,-514,None,None,None,None,None,None,None,-174,-308,-765,None,None,None,None,395,-307,-404,None,366,None,None,None,None,139,2,679,-264,None,-355,684,380,None,-234,-453,872,749,-223,None,None,86,None,786,710,-284,-19,51,-553,None,None,None,393,477,-341,None,None,None,-157,159,-959,656,-335,323,-976,-704,-996,None,-772,34,None,None,-929,327,-532,54,439,114,717,None,None,245,None,None,None,None,1,-118,-814,None,-911,-17,246,-537,-88,298,-135,None,None,None,None,None,None,None,-707,-651,452,None,-836,991,-950,848,923,None,None,None,None,-297,-620,447,-885,None,97,None,None,None,None,None,None,None,None,635,None,None,-781,-982,-366,-100,None,412,None,-56,None,None,None,None,None,-300,-186,None,0,-926,-977,168,None,None,370,None,-612,None,None,None,-677,-453,-947,None,None,322,118,-264,205,-295,None,286,None,None,None,None,897,None,-69,None,None,None,20,-100,-62,None,None,-623,-840,-443,-163,-972,-406,None,-112,None,237,None,None,None,None,None,None,None,252,24,937,None,None,-61,None,None,189,-177,25,-542,None,None,827,None,772,-681,None,None,362,684,130,None,474,315,153,-251,None,None,-919,None,None,None,267,-276,315,-679,None,None,None,None,None,-972,98,546,37,-449,-364,None,20,-206,392,None,522,-906,388,175,-455,65,394,None,-638,680,None,None,-592,-897,-133,493,None,-9,-637,None,-571,367,-70,-811,-771,-575,-929,652,-752,531,-78,-891,329,642,None,-802,None,None,None,None,None,None,None,None,None,None,None,None,None,645,762,None,None,-148,-916,309,None,None,771,-611,None,293,None,313,None,None,807,None,None,None,None,-715,None,None,None,None,None,None,None,-593,-869,905,None,None,None,None,-969,None,612,None,None,None,-576,780,None,-45,691,-927,57,775,-570,892,855,-581,None,-558,-164,-643,-168,597,-945,154,-804,556,None,None,None,-627,None,None,None,None,None,None,None,936,960,None,None,12,22,944,650,-358,None,-163,None,None,None,None,None,None,None,None,None,None,None,-51,None,496,-760,619,-747,406,None,None,997,586,-300,-79,181,None,-763,-435,None,-929,-478,None,-114,456,653,None,-713,651,756,None,-778,-595,None,-548,-411,569,238,None,486,957,None,844,-105,-453,-784,418,725,451,334,874,-238,None,-957,789,-666,-953,-530,507,-579,-170,-586,929,496,-493,33,550,-708,-323,482,-225,None,375,None,None,710,883,None,None,-305,-774,-50,631,None,None,-825,None,-876,899,None,48,None,648,None,308,None,None,None,None,None,None,None,None,None,-166,-947,None,None,None,-971,-918,683,-976,-52,None,646,545,399,-57,None,None,316,None,-535,684,None,None,None,None,-993,483,None,None,None,None,828,None,-310,-645,536,285,562,566,-736,-651,None,None,None,None,None,None,None,None,None,43,291,-952,None,-159,757,837,-306,768,None,None,None,None,None,None,None,None,None,-33,None,None,-703,521,-606,None,-383,-108,933,-555,None,-42,-577,232,895,-340,None,None,852,426,-894,None,-238,103,276,76,None,492,None,None,-766,10,-477,None,-260,None,-543,-580,936,31,-888,-749,984,-188,613,-19,443,None,468,124,6,-688,-546,576,-719,715,-454,-26,-795,180,-742,826,None,733,None,None,None,None,635,None,-940,None,None,638,-829,None,-161,None,None,-682,None,None,122,-377,-528,-813,-223,None,None,None,158,-991,-726,13,-953,None,625,-662,771,None,129,631,-95,825,None,238,None,None,None,None,None,-214,None,-499,-278,-292,-419,None,793,None,None,795,-52,195,-376,-92,888,16,628,-809,None,-831,759,None,826,-367,-75,None,None,None,154,-599,-689,None,942,-925,765,478,328,None,-958,787,None,867,-296,None,None,None,-576,None,817,None,None,640,None,None,799,682,480,-671,-771,656,None,-603,-502,-204,None,773,881,None,931,823,369,None,469,748,None,222,-42,None,None,None,81,None,-775,-258,-743,None,-286,None,-121,-374,-872,-87,None,273,-476,None,None,None,None,None,None,None,-408,None,None,None,-411,587,799,-255,None,-898,962,-403,-108,-648,172,-889,300,-748,-791,-200,627,None,None,None,None,-784,None,-31,None,None,377,-542,146,-763,-951,152,None,-335,None,None,None,None,None,None,None,None,934,-390,-261,-548,837,952,967,None,None,-555,742,-21,None,None,None,None,None,None,-818,910,59,None,None,581,None,-111,None,-406,-956,None,745,-520,967,None,794,875,530,None,332,None,-347,563,647,-505,None,None,None,None,None,None,427,None,-527,930,300,-186,-399,-318,None,None,None,None,None,749,124,862,-104,458,None,None,None,None,None,None,None,None,-979,-572,-916,-329,None,None,-819,-992,-436,None,None,None,872,-555,None,None,None,None,None,937,None,807,571,-984,None,-825,None,None,-465,None,None,None,-904,None,463,-2,-233,729,-118,155,None,None,None,None,3,None,None,None,852,385,None,None,None,-44,-106,None,576,-264,581,None,885,544,-186,None,None,None,358,-666,-403,-516,-716,62,None,None,468,-809,-991,997,-169,None,763,None,-721,None,None,None,None,None,None,None,596,434,None,None,None,None,None,None,None,730,None,-43,923,-187,None,None,-399,266,None,None,55,190,None,-247,None,None,None,None,None,None,None,None,None,-558,243,None,906,929,None,None,-423,None,None,None,None,-102,None,-12,None,None,-689,None,460,530,None,None,None,None,331,-228,None,None,268,-373,-727,-594,None,None,-720,None,None,None,785,-471,917,None,-621,None,832,-135,None,-297,None,433,-292,None,-757,422,197,-931,None,54,None,None,None,None,63,770,-395,105,-421,None,835,-699,None,-530,-210,None,-40,-519,None,None,None,None,-350,-825,-86,None,907,-267,None,None,None,892,827,954,None,None,None,714,-216,-595,None,None,None,None,-18,None,None,None,None,None,145,-533,18,-889,-126,621,805,None,None,-26,None,None,None,None,-6,-544,-126,None,None,None,-506,None,-728,None,373,-742,-571,982,-647,794,None,85,None,120,None,None,754,741,-282,547,None,738,398,219,-425,-935,None,336,-880,-14,None,None,869,-919,None,158,None,None,266,None,None,-433,-869,None,None,None,None,None,None,None,None,361,None,708,None,None,358,-313,345,622,797,-752,None,516,None,None,632,759,-801,867,None,-650,-698,-735,-220,None,-711,-982,None,None,None,None,941,None,-158,122,-391,-2,None,658,-472,938,None,None,None,None,None,None,None,None,None,-888,None,None,483,691,None,None,-685,-712,-669,958,None,200,None,-192,-925,260,-588,-658,-733,990,None,-384,821,557,640,313,None,-154,None,None,None,None,None,None,-850,-591,None,None,318,-438,821,-868,None,394,334,-667,None,-598,None,None,None,301,-955,-570,None,None,-46,828,None,None,292,None,None,None,729,438,None,None,None,118,None,743,None,-924,None,-494,-726,-673,None,-445,None,-695,-475,646,802,None,None,None,732,86,242,789,985,38,None,None,722,None,496,268,None,None,None,None,None,None,None,None,217,None,354,825,None,None,None,836,752,None,-595,-964,-210,-504,279,-299,611,520,107,116,236,-943,179,841,-961,365,-282,-754,None,None,None,326,None,-306,372,-368,337,-728,372,None,None,594,-183,-901,None,537,None,146,None,803,None,-305,247,-619,584,-604,760,199,None,-928,None,-838,60,167,None,None,None,None,None,239,31,None,None,None,-682,52,-294,-607,None,None,-723,None,None,333,519,685,-559,None,210,-440,-599,248,None,None,None,None,None,None,-957,None,None,None,-632,None,976,None,None,-611,None,None,-237,None,None,None,-331,-22,959,None,None,None,None,None,-464,None,None,None,162,206,None,None,42,None,956,None,970,-753,None,None,None,135,179,-643,915,-344,None,None,-758,None,None,-390,None,651,-559,-667,None,-761,-180,33,-491,112,-622,818,None,-909,None,None,None,-592,-66,933,None,None,421,None,None,None,383,None,-611,None,823,711,-270,922,569,-909,333,None,-81,-316,324,-593,-947,None,None,None,224,None,838,None,None,None,None,296,412,None,None,None,436,409,None,None,-151,292,84,325,None,None,None,-772,574,None,978,692,173,-299,None,None,-558,-376,None,None,215,None,459,None,-477,-482,None,None,-320,916,None,None,None,None,None,None,898,None,None,993,-690,547,-623,225,869,527,None,222,814,-221,-237,None,-55,-951,48,None,None,None,None,-285,None,423,None,-64,968,58,676,517,None,868,None,-467,135,-39,None,None,None,-565,734,-995,369,-62,-756,None,None,None,195,189,822,994,None,209,-487,-874,-758,895,147,50,194,None,None,None,None,-897,None,88,-337,-610,866,446,None,-197,-130,-860,476,51,None,-338,-317,351,746,751,None,624,737,865,345,-200,None,None,None,None,898,None,None,None,726,-948,711,None,None,None,475,-729,None,None,899,-375,-639,None,None,-540,197,None,-948,523,None,None,-657,None,151,104,None,-283,None,None,None,260,None,-691,-715,828,None,746,None,-871,None,427,-687,None,939,-893,None,None,711,-551,None,None,-299,None,None,-630,None,None,-394,None,188,None,79,None,-673,11,814,None,-792,-34,None,None,None,-889,None,None,None,None,862,None,239,410,872,493,None,None,None,None,-261,-816,None,None,None,None,None,None,886,344,-907,901,400,-945,750,209,45,646,-194,-952,None,None,584,-945,258,696,None,-281,-98,428,679,696,-745,-690,472,901,407,423,919,None,140,-305,None,885,-666,-91,None,131,None,515,None,429,None,-169,-775,666,None,None,-751,-597,-242,846,499,None,611,611,None,-853,None,None,174,681,190,700,-373,None,411,None,None,None,-428,945,None,None,163,777,None,None,None,None,None,None,None,None,None,None,263,-293,None,None,None,None,None,None,-370,None,None,None,None,34,-407,-545,-268,-497,None,None,None,-700,439,None,-832,None,None,-75,714,-367,-864,None,879,71,852,-781,None,-748,-849,-110,-643,None,654,778,-673,None,None,None,-662,-667,317,None,806,None,None,-605,None,None,None,-380,None,742,None,None,-48,790,991,None,None,None,None,None,885,881,-168,397,None,None,-763,759,-351,-103,None,-867,None,None,None,None,-902,None,None,None,-42,45,829,-781,None,None,None,826,148,-164,None,173,None,None,None,996,-641,336,168,983,123,73,-725,-338,None,890,531,496,-838,-561,None,None,None,None,-193,264,747,-885,None,None,None,None,866,122,None,None,None,None,367,None,382,998,396,702,None,-381,None,None,21,821,None,None,None,None,None,381,None,None,-606,-38,None,None,-280,87,None,472,None,None,None,109,196,253,None,None,959,512,89,503,-902,845,None,None,None,None,None,None,None,-975,None,None,629,114,127,772,-518,682,None,None,-137,None,-519,108,759,211,70,663,86,23,None,-979,950,729,-807,629,None,None,-937,None,-109,-253,-404,None,None,343,None,None,None,None,-586,None,None,-171,None,None,-402,-558,990,768,None,None,None,551,None,-47,847,None,None,None,None,None,38,None,None,None,None,None,502,-895,None,None,-697,None,None,None,None,None,47,904,612,-499,926,-479,-744,-545,None,None,None,None,None,None,198,567,-890,None,None,None,None,None,None,None,None,None,None,None,-113,353,146,-630,719,None,778,None,None,None,None,-971,None,None,None,None,-490,-382,None,-644,None,None,None,449,None,23,None,28,-201,405,None,None,None,-807,None,-917,-604,231,None,None,None,275,None,None,None,None,525,None,None,808,-918,-354,-961,None,793,None,None,None,None,None,None,None,-757,979,None,-464,None,None,None,None,None,None,263,655,206,None,-784,509,None,957,-170,None,None,None,None,None,None,None,None,None,854,920,-968,-629,None,None,None,None,795,-147,None,None,None,None,None,None,None,None,None,None,-439,700,-245,None,None,None,-124,397,-498,None,-646,729,-954,623,-413,-800,None,517,None,-618,994,-137,904,-752,-325,-235,None,-66,None,None,602,938,-915,-154,None,-368,-8,766,-449,-105,None,-376,None,None,820,700,None,None,None,771,None,None,None,None,None,None,None,-202,None,None,None,None,None,564,None,None,None,None,None,None,None,None,None,-517,-892,520,75,-154,None,20,None,None,995,500,-447,-135,None,836,None,None,-627,249,-280,158,-239,628,-55,None,None,None,None,None,374,None,665,None,None,-781,-489,113,None,-506,152,-724,105,-482,None,None,889,None,837,889,None,633,-182,None,229,None,None,None,-69,108,None,777,185,-608,772,990,177,-92,664,968,None,-871,-817,None,-974,-974,601,-790,None,None,-519,None,-155,-859,-719,None,None,None,None,None,0,94,-607,-277,-610,-110,None,None,None,None,None,None,None,None,None,None,286,None,715,None,None,-683,None,None,-194,271,454,None,None,None,None,-262,-524,-218,None,None,None,589,None,None,None,None,None,None,None,900,-418,None,None,None,None,None,-146,None,-802,928,None,834,None,945,None,None,None,-308,None,672,901,482,48,486,None,None,None,None,-933,-122,None,None,None,458,None,-833,None,-780,-841,None,None,None,None,None,None,None,-96,None,None,None,-326,None,None,None,870,None,886,-593,462,None,-46,None,None,None,None,None,None,None,None,None,None,None,None,None,-975,None,None,None,None,-924,511,850,473,None,None,795,-677,None,None,None,-928,None,None,None,578,360,735,None,None,None,None,None,None,404,None,998,-899,None,-253,None,-139,652,703,439,None,None,None,172,None,None,None,None,None,None,None,None,None,947,651,None,-824,645,None,None,None,None,None,None,243,-753,-668,None,745,507,None,None,-394,15,993,None,985,-111,-220,-769,52,554,None,8,898,None,None,711,None,None,None,None,None,586,316,-98,202,-402,377,80,None,608,None,None,-299,177,-767,-193,353,624,None,726,None,None,-879,735,48,None,None,None,812,-482,-920,-942,None,None,None,None,None,None,None,235,None,None,None,None,-177,-685,-567,-961,433,-732,-140,720,415,-230,-355,None,400,None,-657,-871,837,-416,None,-619,752,198,None,None,-847,None,None,None,15,-800,None,None,None,None,-84,713,None,None,None,122,None,None,66,-461,191,-940,-125,-582,-632,165,None,None,None,-186,None,None,-945,None,-122,667,None,865,-190,942,-378,None,892,-945,-256,None,-905,None,None,None,223,None,None,None,None,-768,None,81,None,None,None,-275,103,837,None,-349,501,None,None,None,None,None,None,None,None,None,-501,-100,None,None,None,None,-714,None,None,522,None,None,None,None,None,48,-548,-704,None,None,-430,-55,None,None,-763,None,None,None,None,None,577,None,None,None,-834,981,None,None,31,259,835,728,854,131,75,-681,None,None,863,-827,797,885,755,None,926,None,None,None,None,700,None,None,None,-45,288,770,419,-60,-111,13,-310,None,None,None,None,None,None,34,None,-91,None,None,None,433,None,496,None,-787,858,None,None,-250,None,None,623,-761,None,-560,None,None,None,158,None,-633,None,None,160,None,840,None,-685,None,-540,-310,-279,None,517,111,-11,-923,57,None,None,None,None,None,-686,683,263,None,-56,10,921,384,-923,959,None,652,-332,-588,149,596,None,None,None,663,707,None,None,None,None,-332,-838,-992,None,None,None,None,None,None,-671,-700,None,447,-365,182,-187,-624,-694,-206,654,-214,-234,-210,754,891,None,-607,None,366,None,None,None,None,784,None,None,None,None,None,None,None,None,None,238,None,-909,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-347,244,None,None,None,None,None,None,None,-715,None,None,None,None,-857,-680,113,688,-107,-977,None,-676,-695,-796,737,152,-581,-571,-935,928,968,None,924,None,None,None,None,981,None,None,59,None,None,None,None,None,725,-786,-288,543,None,None,None,-338,None,None,-910,-957,378,None,350,-143,None,None,-531,-981,None,None,699,None,-584,None,-552,-98,None,-887,-214,None,None,None,None,None,None,None,245,-292,None,897,557,527,-964,None,None,None,-196,None,-616,692,-778,None,207,None,None,155,None,None,None,None,-172,None,8,-585,-982,None,937,-306,-136,None,None,350,172,454,None,None,None,None,None,241,None,-975,-986,None,-114,None,None,143,None,819,None,560,-27,None,None,258,None,-501,None,319,None,None,None,None,911,None,None,None,482,None,-514,822,None,None,-533,None,None,None,None,None,None,None,None,None,None,None,None,847,136,559,None,790,None,None,None,None,None,None,249,None,-215,-614,-990,None,None,None,47,-26,-265,None,-869,None,None,121,245,-872,None,None,None,-210,None,948,None,None,-635,346,None,None,374,None,250,-909,None,-470,-997,None,None,None,None,600,None,None,None,None,None,None,None,None,-309,969,290,-774,545,None,-575,None,None,None,None,None,None,None,None,None,None,-124,None,None,None,None,-977,None,567,None,None,None,None,None,None,None,-953,-980,None,None,None,468,-481,250,None,None,None,None,None,115,None,None,None,None,None,None,504,-135,None,670,None,None,None,None,194,None,None,None,-229,None,None,None,None,None,-598,None,None,None,209,166,None,604,None,906,None,373,None,None,None,None,None,None,None,None,None,None,-250,None,None,527,None,-557,164,74,-151,None,None,None,None,None,-613,None,-536,469,None,None,-378,-86,-602,321,None,302,None,None,808,-607,None,None,779,458,None,None,None,230,None,None,-273,-95,None,None,None,None,None,-239,612,-975,-160,None,None,108,None,None,-416,732,-995,-309,223,624,-3,-63,841,872,None,None,-944,None,354,-685,None,None,289,667,614,143,186,-429,-907,None,None,-989,189,None,None,-615,None,None,743,None,-43,None,None,None,None,-112,None,-922,None,None,-960,None,None,None,-146,None,None,None,None,None,-130,None,None,-857,-824,None,None,-426,None,615,None,None,810,481,None,None,None,None,None,None,-705,None,None,428,697,None,-268,None,None,None,833,220,None,None,None,-10,-419,-872,627,None,None,None,None,842,-246,None,None,-394,143,-179,None,669,None,None,None,None,None,None,573,None,None,563,None,-772,None,None,-807,408,None,None,None,663,None,None,993,-798,816,659,None,None,-983,-524,754,113,-526,-866,None,684,None,None,677,677,577,-184,875,803,-194,None,-290,556,None,-105,-375,None,-751,-593,None,655,None,922,None,-327,-94,-903,None,None,-464,314,-817,2,None,None,251,None,None,None,-248,None,574,None,None,None,None,None,-747,None,-183,None,None,None,230,-663,None,828,274,329,249,None,None,None,-250,None,-254,-907,535,None,None,None,215,None,None,None,471,-994,224,966,None,None,-216,-779,None,None,None,None,-913,None,None,None,None,None,124,None,None,None,None,None,-406,-880,-108,-953,None,None,-171,None,None,None,None,None,-683,195,None,636,None,None,None,None,-2,-374,493,786,None,-369,962,None,588,None,None,None,None,None,None,None,None,-365,None,None,None,None,-52,890,None,None,None,-289,None,None,None,-111,None,None,None,None,None,935,-665,-799,None,123,792,-871,893,282,802,415,-571,-439,None,None,-279,-596,-56,928,68,859,33,-82,678,None,275,649,-399,-133,None,None,None,None,-566,None,-307,-43,None,None,329,None,851,662,-97,513,-615,-138,None,None,None,None,-602,282,242,530,-675,-938,None,None,None,None,None,None,43,625,959,None,None,None,351,-364,None,None,None,None,None,None,None,840,None,None,None,None,-579,-293,None,None,-982,351,None,377,-610,326,-811,None,-168,581,-845,-502,912,None,None,None,792,-688,425,None,None,-974,261,317,-127,None,502,905,None,-475,None,-520,None,None,None,None,None,None,None,262,None,None,None,-356,12,829,None,-569,-943,40,None,909,815,-153,None,925,-699,-215,None,None,None,None,842,81,None,None,345,None,None,None,None,355,None,None,None,None,None,None,None,686,22,-192,None,None,None,None,None,7,-663,None,None,None,None,None,None,None,None,None,None,None,654,None,None,226,-150,None,None,None,None,None,None,-951,None,None,None,None,None,None,None,151,-694,None,-159,None,None,-385,-880,None,None,311,None,None,137,115,None,None,None,None,-359,None,611,691,None,None,-477,None,587,None,None,None,None,None,None,824,None,-106,None,171,None,None,None,970,None,-827,-712,84,-83,-815,-70,623,None,541,-301,None,None,None,None,None,None,669,None,None,20,-215,-546,-730,-923,932,-209,540,None,-596,402,-613,None,None,513,718,-43,None,86,0,-450,-973,475,818,251,None,None,None,-705,None,426,130,-762,None,None,-814,360,110,576,366,888,None,472,236,-767,790,298,-931,14,None,364,888,None,None,414,289,-486,480,None,755,-736,-581,344,None,-276,262,None,None,None,None,-142,None,-372,None,None,-7,None,None,-795,625,None,None,337,-28,597,None,-276,-242,None,495,None,-438,150,-402,None,-550,-272,-604,None,None,None,None,None,-541,None,None,-718,None,None,None,None,None,None,None,-487,None,None,-200,None,None,-741,-767,-415,None,704,-513,-345,822,688,484,-352,-130,None,None,-375,None,317,None,-723,164,None,None,None,-246,None,None,-827,-300,None,None,None,None,None,None,None,None,54,None,None,None,316,None,None,None,None,None,-163,None,None,None,None,None,None,None,None,None,None,None,-173,980,None,-766,None,-194,None,-510,None,None,None,-174,None,148,None,None,None,None,None,None,None,None,None,None,None,None,None,-765,None,82,379,None,None,None,439,-177,767,-376,None,-61,8,362,None,678,None,735,556,None,176,86,None,-223,-452,None,-578,None,None,None,None,None,-112,681,None,776,None,None,None,None,None,None,None,None,None,-180,None,None,-140,None,None,222,None,None,None,None,None,None,None,-456,107,-828,None,301,None,None,-213,None,184,753,None,None,642,None,526,None,None,230,None,None,-901,None,None,471,457,-69,-263,None,None,None,None,-964,None,None,-493,None,-416,226,-89,-545,928,-481,-200,-870,None,None,None,None,895,None,None,None,None,None,None,None,-398,12,-29,247,None,None,None,None,None,None,738,-965,None,None,None,None,723,None,-586,-783,None,None,None,None,None,None,None,-417,None,None,None,684,None,-97,None,None,None,None,None,324,54,-610,None,402,None,None,None,None,None,237,None,None,None,-601,None,993,None,None,None,None,None,None,-858,-349,None,None,None,486,785,184,103,None,-546,269,None,None,902,None,None,-82,None,-634,None,None,185,None,-133,348,-277,-810,None,None,None,292,None,241,None,None,None,-553,-351,None,214,877,None,-102,-243,459,-167,-434,68,-758,None,None,-969,None,None,None,-85,-414,19,None,None,None,103,-992,None,-543,679,None,None,None,846,None,324,None,None,None,None,73,622,-740,374,None,-275,-38,None,None,-534,-756,-295,None,270,-618,None,None,None,834,None,None,None,None,None,None,None,88,None,None,635,None,None,None,None,None,437,None,-188,None,None,None,None,-910,None,807,650,-501,None,-577,None,None,-156,470,None,None,None,-824,None,None,293,-29,None,958,-65,-836,None,None,None,None,None,None,None,None,None,689,None,-888,None,-353,813,-842,-333,None,-605,551,None,None,-372,688,None,None,None,968,-185,None,None,None,None,None,-563,-807,-633,-257,None,None,None,-649,None,-2,None,None,416,951,-691,None,90,-765,851,-849,None,None,763,None,None,None,None,None,None,None,None,None,None,-694,None,212,-668,-965,939,None,-392,None,None,None,None,None,-695,None,None,None,None,None,None,None,None,None,None,459,None,-547,615,None,None,None,None,None,None,None,None,None,None,115,238,None,None,None,-880,537,None,None,-227,-372,None,-192,None,989,None,None,-819,None,None,None,-565,None,355,None,None,None,870,None,None,None,None,841,None,None,None,None,None,-994,498,-528,None,None,None,-527,None,None,None,None,None,None,None,None,None,None,-174,None,None,575,None,None,None,236,None,96,None,None,277,-933,395,-630,None,None,None,None,None,364,193,-88,-270,None,None,None,-161,317,765,None,509,None,142,-538,None,245,None,None,-557,140,None,None,None,844,-947,None,None,-96,-902,801,None,-905,595,-636,None,None,546,145,None,None,None,None,None,None,None,None,None,None,830,825,None,None,None,None,947,None,-819,None,283,486,None,None,None,None,None,None,None,None,None,668,None,None,None,None,181,945,None,None,226,391,None,-702,None,None,None,-595,None,None,-985,None,-499,242,-697,490,-5,None,134,None,811,None,-159,None,None,None,879,-97,565,None,None,None,None,-296,None,None,None,485,None,None,-85,None,-410,803,None,398,161,555,None,22,None,None,None,None,None,None,-144,909,148,-789,555,978,None,None,None,-670,925,None,None,594,None,-559,None,64,None,84,None,-372,-874,None,None,None,None,None,None,None,723,933,None,None,971,None,None,None,None,None,None,None,None,None,None,-951,None,None,None,-802,-979,None,566,601,None,None,-633,-719,None,226,None,None,None,None,None,None,None,None,None,509,None,463,-234,None,None,None,214,None,774,None,-971,-961,247,126,None,None,-329,-937,115,118,-990,-531,705,None,128,-325,None,255,None,None,None,None,None,-56,666,None,None,-60,None,None,None,None,-816,-969,None,-666,None,-435,None,-48,261,None,916,None,None,-36,None,None,None,462,None,-802,None,None,None,None,-671,363,None,None,None,None,-960,-583,98,726,None,None,None,None,None,None,-963,-340,None,None,348,None,None,460,None,318,-542,-367,-568,-653,-416,915,586,-249,191,None,None,None,None,None,561,538,482,160,944,-492,80,457,-831,733,600,-668,-371,-334,None,None,None,None,None,None,None,None,None,None,None,None,None,837,-103,820,736,None,219,386,-535,-69,740,85,514,-918,None,880,951,None,396,None,None,299,233,-374,117,587,-936,372,-463,892,None,None,None,None,None,None,224,None,60,55,492,741,275,None,None,-463,None,None,None,658,642,476,-953,None,651,-435,None,None,None,None,None,None,-4,None,None,None,-434,911,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,68,301,None,None,-38,None,None,404,None,None,617,979,None,None,63,-806,639,None,-233,None,-856,-106,None,None,-223,None,-76,84,None,None,None,None,-465,221,728,-48,-517,267,None,None,327,None,None,None,None,None,-599,None,None,None,None,None,None,None,None,None,None,460,None,None,None,-742,None,None,None,None,None,None,None,None,-646,-245,-171,271,None,None,-734,None,None,None,None,None,751,None,-848,-910,-447,None,-590,None,None,None,213,-857,320,-173,227,None,None,None,None,None,None,None,None,None,None,None,901,743,446,None,None,None,None,None,None,None,None,None,328,None,-917,None,None,None,282,None,None,None,None,None,None,628,None,-691,None,None,None,None,829,-933,None,-808,None,None,None,None,None,None,None,613,None,None,-271,-902,227,None,None,None,None,None,None,-564,-338,None,None,None,None,-405,None,None,967,-866,-550,None,None,None,None,None,None,None,None,None,None,-52,None,550,None,None,-398,732,-420,None,-761,966,379,None,438,-672,None,588,None,None,None,851,None,637,675,None,None,-986,None,None,None,None,None,None,None,None,-628,65,None,None,82,982,None,None,45,None,None,None,None,None,None,None,None,None,-78,None,None,None,None,None,None,None,None,None,845,None,None,None,-555,None,None,-438,None,None,-418,None,None,None,None,None,None,None,None,None,None,-103,-928,None,None,-951,None,-459,None,None,676,None,480,None,None,None,None,None,-791,262,-137,None,None,None,None,None,None,414,464,None,-420,None,None,None,None,None,None,None,None,None,None,None,None,None,256,27,-953,-638,872,-420,None,None,None,None,465,127,-29,None,344,None,-545,175,-539,62,None,None,None,573,None,None,-16,-444,335,None,None,None,None,None,-233,None,None,None,None,None,None,None,None,None,None,None,-303,-47,815,None,59,None,None,None,-479,652,-619,None,None,None,None,49,559,None,None,-705,None,None,750,None,-695,684,-659,-317,-358,None,None,-483,None,None,None,None,None,-210,None,None,None,-982,None,None,None,-540,None,None,-14,176,None,None,541,706,None,None,None,None,None,None,191,39,None,372,None,824,None,None,-856,-279,None,-310,None,-496,None,None,-194,None,-27,242,None,None,None,-486,None,None,416,None,414,-333,-219,None,-356,None,None,None,None,None,None,None,None,None,None,None,920,-352,None,None,None,None,None,None,None,-742,None,574,None,None,None,-428,None,None,-990,None,None,None,None,None,None,-178,47,-353,None,None,None,None,None,None,None,None,None,205,None,None,-795,-721,None,None,-463,-182,-100,-763,None,None,None,None,None,None,88,-225,None,-232,None,None,None,None,776,None,337,-572,None,-142,None,989,112,None,None,731,-51,569,None,231,None,None,-712,None,None,None,None,-37,210,None,None,None,-88,None,None,-567,None,-334,None,None,None,None,None,None,542,397,None,None,None,None,None,None,280,None,None,None,None,None,87,745,324,-549,-807,232,979,None,578,None,118,None,-109,None,-787,159,758,-45,-110,-43,None,None,404,None,-723,-23,546,None,None,268,-33,None,None,None,-183,None,None,474,None,None,None,None,None,258,None,None,None,None,-101,67,None,None,None,101,None,-532,None,None,642,589,-240,389,None,None,-684,None,-499,-943,-433,673,205,713,None,165,-679,None,None,None,None,None,-69,-761,None,-427,224,-298,None,-9,191,400,222,None,376,847,269,-604,None,571,696,417,None,None,None,-833,809,None,-564,None,68,433,747,235,296,-869,None,None,None,-283,None,96,None,-859,None,None,None,-269,None,None,82,287,221,564,49,-840,302,None,641,-953,628,905,631,882,294,625,None,None,359,None,None,None,-92,-582,387,None,990,-725,None,-541,None,None,None,None,None,None,-661,844,179,965,-622,-70,None,-83,186,None,-742,-1,None,None,-198,80,None,None,None,None,None,265,-349,-683,None,None,920,None,None,-758,None,None,None,None,-69,630,None,-539,223,-872,556,None,None,683,None,-181,300,None,None,747,-166,679,-50,736,-953,-632,None,949,None,406,-426,696,None,-28,-676,None,252,-362,479,-627,-562,-826,None,-862,None,-38,7,919,-20,None,-397,None,None,None,None,None,None,None,None,None,None,678,None,None,-18,None,None,-587,None,None,None,None,None,-420,None,None,-619,None,None,-819,-181,None,None,None,518,None,None,None,655,-924,959,410,None,-274,None,None,None,None,None,None,None,None,-779,None,None,None,None,-297,None,None,-428,None,439,None,-698,None,None,-528,None,258,None,None,None,None,None,-79,None,None,-630,None,None,None,None,-481,None,None,None,None,None,None,-139,493,908,555,None,None,None,-980,-757,-568,None,None,None,None,280,-492,None,None,None,None,None,-448,None,None,None,None,None,-533,None,76,None,None,None,None,None,None,None,-494,None,None,None,None,None,None,None,904,8,526,-405,None,358,912,None,121,-59,143,None,-525,None,None,None,None,None,-311,-220,None,None,-224,None,-622,None,-968,192,None,None,None,None,-718,-162,None,None,None,None,-40,None,None,-893,None,None,-734,None,None,None,None,-976,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-784,-523,None,None,None,None,788,42,None,741,305,None,180,None,739,None,-99,426,None,None,591,None,None,-917,None,None,None,-23,-110,950,None,None,-590,None,None,-576,None,374,None,-401,None,None,None,None,620,710,None,None,None,674,851,None,None,-977,None,None,None,-900,933,-561,-896,None,728,310,-175,454,None,None,None,None,None,None,None,-49,None,-978,765,-390,None,-127,None,None,None,None,None,None,None,None,879,975,None,None,None,None,None,None,None,None,-990,-591,None,-938,None,None,None,None,None,None,-24,None,439,-855,None,None,244,None,-809,19,None,None,None,None,None,None,None,-366,None,None,None,None,-655,None,None,None,-19,None,-452,None,None,None,None,309,None,None,None,190,-430,484,129,None,666,-854,897,None,492,223,-409,None,None,-344,None,None,None,None,None,None,576,-117,769,-913,509,None,None,331,None,None,None,-4,None,None,None,-251,None,-594,None,None,None,None,None,None,None,None,None,914,None,-787,-837,None,730,None,None,None,-68,None,431,-70,None,-804,None,None,None,None,None,None,None,None,None,249,411,626,None,None,None,None,-385,3,None,937,None,470,-885,None,None,-721,-591,-881,786,891,543,None,574,70,None,-728,-735,-693,None,370,-360,-316,-817,-233,-865,0,-771,-242,None,None,None,None,None,None,-157,None,None,None,None,420,-103,-932,766,13,None,None,None,-738,None,-786,-154,712,-782,None,None,None,None,None,None,None,None,None,None,None,None,727,-705,-715,-997,-831,-458,None,None,None,None,None,416,-142,None,652,None,None,897,821,474,577,309,-489,-889,-436,-483,695,-804,None,None,-965,None,-488,None,276,72,None,None,-365,None,None,822,-756,None,None,None,None,None,-963,73,879,953,872,-82,923,860,None,-876,None,None,None,None,-14,None,None,-688,-870,None,863,None,-432,641,None,None,315,None,None,656,None,None,None,None,-835,None,None,None,613,None,None,-107,-233,None,None,955,None,None,-784,-410,None,-833,3,None,None,None,676,None,None,None,None,None,41,None,None,None,None,None,None,None,None,None,841,None,15,116,-633,None,-834,None,None,None,None,965,None,None,None,None,None,127,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,994,None,None,-613,None,None,None,None,-506,911,None,-306,None,None,None,None,None,None,-737,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-510,None,None,-514,None,659,-875,None,None,None,None,983,None,None,-275,735,-350,None,None,None,518,None,None,None,None,None,None,None,-379,None,None,None,-796,None,None,None,None,-465,None,None,None,None,None,None,335,None,None,193,None,565,357,None,None,None,113,None,None,-918,None,None,None,None,-809,None,None,-850,None,-379,None,None,616,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-84,-686,-485,None,None,None,-722,-591,-798,-453,None,-416,None,None,None,None,872,-957,None,None,None,None,None,None,None,None,434,None,None,None,None,-918,None,675,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,982,None,None,None,None,None,None,None,-260,None,None,None,None,None,None,None,None,879,None,None,None,None,None,None,546,None,None,-676,-5,993,None,None,None,None,None,None,None,None,-951,531,968,None,None,387,None,None,-889,None,None,-275,None,None,-915,-779,-706,None,-730,None,None,None,None,869,None,473,58,None,None,None,-621,None,None,682,631,682,None,None,None,None,None,968,169,None,None,None,None,None,None,None,None,-358,None,None,None,None,None,None,None,-78,None,None,None,None,None,None,None,None,-949,-190,None,-385,None,-409,644,None,None,None,-101,194,None,840,None,-862,436,739,258,None,-465,-265,361,749,600,543,None,None,None,None,None,-278,-934,-413,925,None,670,-374,-575,193,None,None,382,-240,None,-398,None,691,458,-31,None,-367,None,None,-198,-924,None,113,None,-662,None,None,None,-222,None,122,422,-385,-120,899,503,105,None,None,None,None,-579,None,None,-780,557,None,-327,-701,-810,None,None,None,-787,-982,None,869,None,None,-541,-84,-414,574,-331,-78,109,None,445,None,-877,None,None,575,None,-447,528,-900,None,None,35,508,None,None,618,None,None,None,None,None,None,-347,None,None,748,200,401,143,None,-143,-694,213,None,953,None,None,None,None,None,-160,None,410,-41,911,None,-742,None,None,None,279,None,None,None,None,None,None,None,None,-67,588,None,None,746,None,None,None,None,None,None,None,540,None,-569,None,None,None,None,-366,None,None,None,None,22,None,-727,-473,None,None,None,-933,None,-542,-77,None,None,None,-225,None,None,-863,None,None,None,None,None,None,None,215,None,None,739,-396,None,None,None,None,-42,-937,None,-104,None,-752,None,None,None,-580,None,255,None,None,None,None,None,None,None,None,191,None,None,None,None,None,-282,None,None,None,None,784,-606,None,None,None,231,None,None,None,None,None,858,None,880,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,211,None,-313,None,None,None,-264,None,None,None,None,None,None,None,None,665,866,None,None,None,None,None,389,70,None,None,None,None,-865,-404,-747,None,None,None,None,None,None,None,None,None,None,None,None,None,None,822,None,-141,None,None,None,None,-579,44,None,None,168,None,-735,None,849,513,-33,None,None,984,None,None,None,-790,None,None,None,None,None,None,None,None,236,None,-3,None,58,None,None,-824,None,-165,862,-822,44,None,512,None,887,707,374,375,None,None,None,None,None,None,-931,None,-957,-174,-204,-98,902,340,None,None,-220,None,None,None,883,638,None,None,None,None,None,None,None,None,None,None,None,-91,None,None,None,None,44,None,None,None,None,None,448,None,358,None,None,None,None,None,None,-695,None,205,-557,-279,None,None,-710,None,None,220,620,-471,977,None,-968,906,503,None,None,None,227,591,144,None,-70,None,None,926,None,None,None,None,None,None,None,None,None,None,None,None,-677,None,-678,162,-636,485,316,-883,None,None,None,263,None,-589,None,None,None,None,None,None,-22,None,-644,121,-42,None,None,None,None,None,None,None,896,None,None,None,None,None,None,840,None,None,792,None,None,None,-389,None,-305,853,None,None,None,None,None,199,None,946,654,None,908,None,None,-827,27,None,None,None,None,None,None,None,None,None,None,None,-508,None,None,None,None,None,None,None,None,754,None,None,None,None,40,None,None,-38,None,634,-347,None,None,-260,None,None,None,90,None,-701,None,-295,None,-176,None,None,None,-568,-38,None,None,-838,None,None,659,None,-136,-793,None,None,None,None,-981,-356,-986,None,None,-947,381,None,None,-580,None,None,None,None,None,None,None,540,None,394,-289,None,None,-502,None,None,None,None,-231,-648,-282,None,None,None,297,913,777,-999,None,None,461,None,None,-901,-169,None,-942,None,None,None,None,None,None,None,None,None,-350,None,None,956,None,-720,None,None,292,-879,None,None,134,158,None,-144,568,None,None,None,None,None,None,-741,962,None,-872,-215,None,None,None,None,None,None,None,None,-185,228,None,241,214,None,None,985,822,947,None,828,587,None,-838,None,None,349,None,767,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,55,None,864,None,None,-279,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-823,266,-413,-392,None,-17,None,None,None,-414,None,-897,590,None,-757,None,764,None,None,-290,-931,None,None,10,None,None,-762,None,None,None,498,497,None,None,None,None,None,None,20,547,376,None,None,None,415,-406,None,None,None,-728,387,None,-153,-83,None,-105,-347,None,None,None,None,None,None,296,-632,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,451,None,None,None,None,983,None,-646,-941,-359,None,-13,None,None,214,-282,884,223,None,None,None,None,None,-91,None,None,-50,None,None,None,None,None,84,None,None,None,None,None,None,None,None,535,None,None,None,None,None,None,None,None,None,-390,-469,None,None,956,None,None,310,-146,None,149,None,-145,None,372,None,766,-208,None,None,-909,None,None,190,None,588,792,None,None,None,None,940,None,None,None,-818,840,None,-511,None,-669,-8,None,None,None,None,637,961,292,None,None,None,None,None,-689,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,650,-331,None,None,None,-258,None,-438,None,None,None,None,None,None,None,None,None,None,-240,438,None,None,666,None,None,None,None,None,-704,None,None,None,None,305,-510,-136,None,None,None,None,None,None,None,None,None,178,None,None,None,None,None,-589,None,960,None,192,None,908,None,None,None,None,-124]]
	input_sum = [155]
	expected_output = [True]
	
	for i in range(len(input_root)):
		if hasPathSum(List2TreeNode(input_root[i]),input_sum[i]) != expected_output[i]:
			print("Wrong!!!")
			print(hasPathSum(List2TreeNode(input_root[i]),input_sum[i]))
		else:
			print("Right")		
	# print(hasPathSum(List2TreeNode(input_root[-1]),input_sum[-1]))