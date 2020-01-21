package main


import (
	"strings"
	"fmt"
)

//557
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

//557
func main() {
	s := "Let's take LeetCode contest"
	fmt.Println(reverseWords(s))	
}
