// ToDo:
/* */

// Problem Description
/*
557. Reverse Words in a String III
Easy

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string. 
*/

// Conditions & Concepts
/* */

// Code
// submit part
// func reverseWords(s string) string {
	
// }
// test part */
/* */

// code here
// 1
/* 
import (
	"strings"
)

func reverseWords(s string) string {
	s := strings.Split(s," ")
	s1 = string
	for i, word := range s {
		// reverse()
		runes := []rune(word)
		for from, to := 0, len(runes)-1; from < to; from, to = from+1, to-1 {
			runes[from], runes[to] = runes[to], runes[from]
		// s[i] = string(runes)
		s1 := s + " " + s1
		}		
	}
	return s1	
}
*/

// 1.1

// import (
// 	"strings"
// )

// func reverseWords(s string) string {
// 	s1 := strings.Split(s," ")
// 	var s2 string
// 	for word := range s1 {
// 		// reverse()
// 		runes := []rune(word) //cannot convert word (type int) to type []rune (solution.go)
// 		for from, to := 0, len(runes)-1; from < to; from, to = from+1, to-1 {
// 			runes[from], runes[to] = runes[to], runes[from]
// 		// s[i] = string(runes)
// 		s2 := s + " " + s2
// 		}		
// 	}
// 	return s2	
// }


//1.25
/*
func main() {
	s := "Let's take LeetCode contest"
	fmt.Print(strings.Split(s," "),"\n")
	fmt.Println(strings.Split(s," "))
	fmt.Println(len(strings.Split(s," "))) //4
	fmt.Printf("%q\n",strings.Split(s," "))	
}

// [Let's take LeetCode contest]
// [Let's take LeetCode contest]
// ["Let's" "take" "LeetCode" "contest"]
*/

//1.2
/*
Wrong Answer
Your input:" "
Output:" "
Expected:""
*/
import (
	"strings"
)

func reverseWords(s string) string {
	s1 := strings.Split(s," ")
	var s2 string
	for _, word := range s1 {
		var s3 string
		for _, alph := range string(word) {
			s3 = string(alph) + s3
		}
		s2 = s2 + " " + s3 //
	}
	return s2[1:]
}

//1.21
/*
Wrong Answer
Your input: "  Let's take LeetCode contest  "
Output: ""
Expected: "s'teL ekat edoCteeL tsetnoc"
*/
import (
	"strings"
)

func reverseWords(s string) string {
	s = string.Trim(s, " ")
	s1 := strings.Split(s," ")
	var s2 string
	for _, word := range s1 {
		var s3 string
		for _, alph := range string(word) {
			s3 = string(alph) + s3
		}
		if s3 != "" {
			s2 = s2 + " " + s3
		} else {
			s2 = s3
		}
		
	}
	return s2	
}

//1.22
/*
Wrong Answer
Your input: "  Let's take LeetCode contest  "
Output: " s'teL ekat edoCteeL tsetnoc"
Expected: "s'teL ekat edoCteeL tsetnoc"


Success
Runtime: 36 ms, faster than 22.32% of Go online submissions for Reverse Words in a String III.
Memory Usage: 7.6 MB, less than 100.00% of Go online submissions for Reverse Words in a String III.
*/
import (
	"strings"
)

func reverseWords(s string) string {
	s = strings.Trim(s, " ")
	s1 := strings.Split(s," ")
	var s2 string
	for _, word := range s1 {
		var s3 string
		for _, alph := range string(word) {
			s3 = string(alph) + s3
		}
		if s2 != "" { 
			s2 = s2 + " " + s3
		} else {
			s2 = s3
		}
		
	}
	return s2	
}

//test
package main

import (
	"strings"
	"fmt"
)

func reverseWords(s string) string {
	s1 := strings.Split(s," ")
	var s2 string
	for _, word := range s1 {
		var s3 string
		for _, alph := range string(word) {
			s3 = string(alph) + s3
		}
		if s3 != "" {
			s2 = s2 + " " + s3
		} else {
			s2 = s3
		}
		
	}
	return s2	
}

func main() {
	s := "Let's take LeetCode contest"
	fmt.Println(reverseWords(s))	
}