#35
def searchInsert(nums, target):	
	if len(nums) == 0:
		return 0
	else:
		if target < nums[0]:
			return 0
		elif target > nums[-1]:
			return len(nums)
		else:
			for i in range(len(nums)):
				if nums[i] == target:
					return i
				elif target < nums[i]:
					return i

if __name__ == "__main__":
    #35
	input_nums = [
	[1,3,5,6],
	[1,3,5,6],
	[1,3,5,6],
	[1,3,5,6]
	]
	input_target = [5,2,7,0]
	expected_output = [2,1,4,0]
	for i, j in enumerate(input_nums):
		if searchInsert(input_nums[i],input_target[i]) != expected_output[i]:
			print("Wrong!!!")
			print(searchInsert(input_nums[i],input_target[i]))
		else:
			print("Right")		
	# print(searchInsert(input_nums[-1],input_target[-1]))