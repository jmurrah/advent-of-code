package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.ReadFile("input.txt")
	var leftNumbers, rightNumbers []int
	similarityScores := make(map[int]int)

	for _, line := range strings.Split(string(file), "\n") {
		numbers := strings.Fields(line)
		left, _ := strconv.Atoi(numbers[0])
		right, _ := strconv.Atoi(numbers[1])
		similarityScores[left] = 0
		leftNumbers = append(leftNumbers, left)
		rightNumbers = append(rightNumbers, right)
	}

	for i := range rightNumbers {
		if _, exists := similarityScores[rightNumbers[i]]; exists {
			similarityScores[rightNumbers[i]] += 1
		}
	}

	output := 0
	for key, value := range similarityScores {
		output += key * value
	}

	fmt.Println(output)
}
