package main

import (
	"fmt"
	"strconv"
	"strings"
)

// 557
func reverseWords(s string) string {
	s1 := strings.Split(s," ")
	var s2 string
	for _, word := range s1 {
		var s3 string
		for _, alph := range string(word) {
			s3 = string(alph) + s3
		}
		s2 = s2 + " " + s3
	}
	return s2	
}

//func main() {
//	s := "Let's take LeetCode contest"
//	fmt.Println(reverseWords(s))
//}

// 581
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

func findUnsortedSubarray(nums []int) []int {
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
	return nums[start_i:end_i]
}

//func main() {
//	fmt.Println(findUnsortedSubarray([]int{2,3,3,2,4}))
//}


//594
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

func main(){
	fmt.Println(findLHS([]int{1,3,2,2,5,2,3,7}))
}