// ToDo:
/* */

// Problem Description
/*
594. Longest Harmonious Subsequence
Easy

We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.
*/

// Conditions & Concepts
/* */

// Code
// submit part
func findLHS(nums []int) int {
    
}
// test part
/* */

// code here
// 1
/*
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.
 */
func findLHS(nums []int) int {
	medium := false
	m := make(map[string]int)
	for _, num := range nums {
		if _, ok := m[strconv.Itoa(num)]; ok{
			m[strconv.Itoa(num)] += 1
		} else {
			m[strconv.Itoa(num)] = 1
		}
	}
	count := 0
	for _, c := range m {
		if c %2 == 0{
			count += c
		} else if c > 2 {
			count += c -1
			medium = true
		} else {
			medium = true
		}
	}
	if medium == true {
		return count + 1
	}
	return count
}

//1.1
func findLHS(nums []int) int {
	m := make(map[string]int)
	for _, num := range nums {
		if _, ok := m[strconv.Itoa(num)]; ok{
			m[strconv.Itoa(num)] += 1
		} else {
			m[strconv.Itoa(num)] = 1
		}
	}
	max_count := 0
	for i, c := range m {
		if (count, ok := m[strconv.Itoa(strconv.Atoi(i)+1)]; ok || count, ok := m[strconv.Itoa(strconv.Atoi(i)-1)]; ok) {
			if (count %2 != 0 && c %2 != 0) {
				sum := c + count - 1
			} else {
				sum := c + count
			}
			if max_count < sum {
				max_count = sum
			}
		}
	}
	return max_count
}

// Test
package main

import (
	"fmt"
)

func main(){
	fmt.Println(findLHS([]int{1,3,2,2,5,2,3,7}))
}