// ToDo:
/* */

// Problem Description
/*
561. Array Partition I
Easy

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:

n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

*/

// Conditions & Concepts
/* */

// Code
// submit part
func arrayPairSum(nums []int) int {
	
}

// test part
/* */

// code here
// 1
/* 
[quickSort()](https://github.com/TheAlgorithms/Go/blob/master/sorts/quick_sort.go)

Success
Runtime: 96 ms, faster than 15.33% of Go online submissions for Array Partition I.
Memory Usage: 7.8 MB, less than 100.00% of Go online submissions for Array Partition I.
*/
func quickSort(arr []int) []int {

	if len(arr) <= 1 {
		return arr
	}

	median := arr[rand.Intn(len(arr))]

	low_part := make([]int, 0, len(arr))
	high_part := make([]int, 0, len(arr))
	middle_part := make([]int, 0, len(arr))

	for _, item := range arr {
		switch {
		case item < median:
			low_part = append(low_part, item)
		case item == median:
			middle_part = append(middle_part, item)
		case item > median:
			high_part = append(high_part, item)
		}
	}

	low_part = quickSort(low_part)
	high_part = quickSort(high_part)

	low_part = append(low_part, middle_part...)
	low_part = append(low_part, high_part...)

	return low_part
}

func arrayPairSum(nums []int) int {
	a_b := quickSort(nums)
	a_sum := 0
	for i, num := range a_b {
		if i%2 ==0{
			a_sum += num
		}
	}
	return a_sum
}

// Test
package main

import (
	"fmt"
)

func main() {
	input_nums := [][]int{{1,4,3,2}, {1,2,3,4}}
	output_int := []int{4, 4}
	for i, nums := range input_nums {
		if arrayPairSum(nums) == output_int[i] {
			fmt.Println("Sample",i," is Right.")
		} else {
			fmt.Println("Sample",i," is Wrong! /n Output:",arrayPairSum(nums), "/n Expected Output:", output_int[i]))
		}
	}

	fmt.Println("Hello Word")
}
