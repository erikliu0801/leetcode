// ToDo:
/* */

// Problem Description
/*
566. Reshape the Matrix
Easy

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:

Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:

	The height and width of the given matrix is in range [1, 100].
	The given r and c are all positive.

*/

// Conditions & Concepts
/* */

// Code
// submit part
func matrixReshape(nums [][]int, r int, c int) [][]int {
	
}
// test part */
/* */

// code here
// 1
/*
func main() {
	nums := [][]int{
		[]int{1,2},
		[]int{3,4},
	}
	fmt.Println(len(nums))
	fmt.Println(len(nums[0]))
	fmt.Println(len(nums) * len(nums[0]) == 2 * 2) //true
	fmt.Println(nums[0],nums[1]...) //"..." is the syntax
}
*/
import (
	""
)

func matrixReshape(nums [][]int, r int, c int) [][]int {
	nums_r, nums_c := len(nums), len(nums[0])
	if nums_r * nums_c != r * c {
		return nums
	} else {		
		for i := 1; i <= len(nums)-1; i++{
			nums[0] = append(nums[0],nums[i]...)
		}
		for i := 0; i <= len(nums[0]); i++{
			if (i/c)+1 <= len(nums) && i%c <= nums_c-1 {
				nums[(i/c)+1][i%c] = nums[0][i] //index out of range
			
			} else if (i/c)+1 > len(nums){
				nums = append(nums,[]int{nums[0][i]}) 
			
			} else { //i%c > nums_c
				nums[(i/c)+1] = append(nums[(i/c)+1], nums[0][i]) 

			}	
		}
		return nums[1:]
	}	
}

//1.1
/*
Success
Runtime: 64 ms, faster than 44.62% of Go online submissions for Reshape the Matrix.
Memory Usage: 91.6 MB, less than 100.00% of Go online submissions for Reshape the Matrix.
*/
func matrixReshape(nums [][]int, r int, c int) [][]int {
	nums_r, nums_c := len(nums), len(nums[0])
	if nums_r * nums_c != r * c {
		return nums
	} else {		
		var nums1 []int
		for i := 0; i <= len(nums)-1; i++{
			nums1 = append(nums1,nums[i]...)
		}
		var nums2 [][]int
		for i := range nums1{
			if i/c > len(nums2)-1{
				nums2 = append(nums2,[]int{nums1[i]})
			} else {
				nums2[i/c] = append(nums2[i/c],nums1[i])
			}
		}
		return nums2
	}
}


// Test
package main

import (
	"fmt"
)

func matrixReshape(nums [][]int, r int, c int) [][]int {
	nums_r, nums_c := len(nums), len(nums[0])
	if nums_r * nums_c != r * c {
		return nums
	} else {		
		var nums1 []int
		for i := 0; i <= len(nums)-1; i++{
			nums1 = append(nums1,nums[i]...)
		}
		var nums2 [][]int
		for i := range nums1{
			if i/c > len(nums2)-1{
				nums2 = append(nums2,[]int{nums1[i]})
			} else {
				nums2[i/c] = append(nums2[i/c],nums1[i])
			}
		}
		return nums2
	}
}

func main() {
	nums := [][]int{
		[]int{1,2},
		[]int{3,4},
	}
	fmt.Println(matrixReshape(nums,1,4))
}