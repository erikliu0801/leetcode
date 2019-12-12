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

#38
def countAndSay(n):
	start = '1'
	if n > 1:
		# answer = ''
		for m in range(n-1):
			count = 1
			answer, repeat = '', ''
			for i in range(len(start)):
				if i == 0:
					repeat = start[i]
				elif start[i] == repeat:
					count += 1
				elif start[i] != repeat:
					answer = answer + str(count) + str(start[i-1])
					repeat = start[i]
					count = 1
			answer = answer + str(count) + str(start[-1])
			start = answer
		return answer
	else:
		return start



if __name__ == "__main__":
    #35
	# input_nums = [
	# [1,3,5,6],
	# [1,3,5,6],
	# [1,3,5,6],
	# [1,3,5,6]
	# ]
	# input_target = [5,2,7,0]
	# expected_output = [2,1,4,0]
	# for i, j in enumerate(input_nums):
	# 	if searchInsert(input_nums[i],input_target[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(searchInsert(input_nums[i],input_target[i]))
	# 	else:
	# 		print("Right")		
	# print(searchInsert(input_nums[-1],input_target[-1]))

    #38
    input1 = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_output = ["1", "11", "21", "1211", "111221", "312211", "13112221", "1113213211"]

    for i, j in enumerate(input1):
        if countAndSay(input1[i]) != expected_output[i]:
            print("Wrong!!!")
            print(countAndSay(input1[i]))
        else:            
            print("Right")
    # print(countAndSay(input1[1]))