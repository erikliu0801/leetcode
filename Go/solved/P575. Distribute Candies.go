// ToDo:
/* */

// Problem Description
/*
575. Distribute Candies
Easy
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:

Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 

Example 2:

Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 

Note:

    The length of the given array is in range [2, 10,000], and will be even.
    The number in given array is in range [-100,000, 100,000].
*/

// Conditions & Concepts
/* */

// Code
// submit part
func distributeCandies(candies []int) int {
    
}
// test part
/* */

// code here
// 1
/* 
Success
Runtime: 528 ms, faster than 5.56% of Go online submissions for Distribute Candies.
Memory Usage: 6.7 MB, less than 100.00% of Go online submissions for Distribute Candies.
*/
func seqsearch(nums []int, num int) int {
	var i int
	for i=0; i < len(nums) ; i++ {
		if nums[i] == num {
			return i
		}
	}
	return -1
}

func distributeCandies(candies []int) int {
	if len(candies)%2 != 0 {
		return 0
	}
	var sis []int
	for _, candy := range candies {
		switch {
			case len(sis) >= len(candies)/2 :
				return len(candies)/2
			case seqsearch(sis, candy) == -1 :
				sis = append(sis, candy)
		}
	}
	return len(sis)
}

// Test
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello Word")
}
