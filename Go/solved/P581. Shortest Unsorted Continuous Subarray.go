// ToDo:
/* */

// Problem Description
/*
581. Shortest Unsorted Continuous Subarray
Easy

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:

	Then length of the input array is in range [1, 10,000].
	The input array may contain duplicates, so ascending order here means <=.
*/

// Conditions & Concepts
/* */

// Code
// submit part
func findUnsortedSubarray(nums []int) int {
	
}
// test part
/* */

// code here
// 1
/*
Wrong Answer
Input: [2,3,3,2,4]
Output: 2
Expected :3
 */
func max(nums []int) int {
	c := nums[0]
	for _, c0 := range nums {
		if c0 > c {
			c = c0
		}
	}
	return c
}

func findUnsortedSubarray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	var start_i, end_i int
	start_c := nums[0]
	for i, c := range nums {
		if c < start_c {
			start_i = i-1
			break
		} else {
			start_c = c
		}
	}
	for i := len(nums) -1 ; i > start_i ; i-- {
		if nums[i] != max(nums[:i+1]) {
			end_i = i+1
			break
		}
	}
	return len(nums[start_i:end_i])
}

//2
/*
Success
Runtime: 244 ms, faster than 5.75% of Go online submissions for Shortest Unsorted Continuous Subarray.
Memory Usage: 6.4 MB, less than 100.00% of Go online submissions for Shortest Unsorted Continuous Subarray.
*/
func min(nums []int) int {
	c := nums[0]
	for _, c0 := range nums {
		if c0 < c {
			c = c0
		}
	}
	return c
}

func max(nums []int) int {
	c := nums[0]
	for _, c0 := range nums {
		if c0 > c {
			c = c0
		}
	}
	return c
}

func findUnsortedSubarray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	var start_i, end_i int
	for i := 0 ; i < len(nums)-1 ; i++ {
		if nums[i] != min(nums[i:]) {
			start_i = i
			break
		}
	}
	for i := len(nums) -1 ; i > start_i ; i-- {
		if nums[i] != max(nums[:i+1]) {
			end_i = i+1
			break
		}
	}
	return len(nums[start_i:end_i])
}

// Test
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello Word")
}
