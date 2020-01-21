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
/* */
import (
	""
)

func findUnsortedSubarray(nums []int) int {
	var start_i, end_i int, int
	start_c, end_c := nums[0], nums[-1]
	for i, c := range nums {
		if c < start_c {
			start_i = i
			break
		} else {
			star_c = c
		}
	}	
	for i:= 1 ; ; i++ {
		switch {
			case i >= len(nums) - start_i:
				return  nums[start_i:-1]

			case nums[-i] < end_c:
		}
	}

	return nums[start_i:end_i]
}

// Test
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello Word")
}
