package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func find_number(line string) string {
	for _, character := range line {
		if unicode.IsDigit(rune(character)) {
			return string(character)
		}
	}
	return ""
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	file, _ := os.ReadFile("input.txt")

	total := 0
	for _, line := range strings.Split(string(file), "\n") {
		num, _ := strconv.Atoi(find_number(line) + find_number(reverse(line)))
		total += num
	}

	fmt.Println(total)
}
