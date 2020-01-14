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
func reverseWords(s string) string {
	
}
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
import (
	"strings"
)

func reverseWords(s string) string {
	s1 := strings.Split(s," ")
	var s2 string
	for word := range s1 {
		// reverse()
		runes := []rune(word) //cannot convert word (type int) to type []rune (solution.go)
		for from, to := 0, len(runes)-1; from < to; from, to = from+1, to-1 {
			runes[from], runes[to] = runes[to], runes[from]
		// s[i] = string(runes)
		s2 := s + " " + s2
		}		
	}
	return s2	
}