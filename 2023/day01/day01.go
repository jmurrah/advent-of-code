package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func find_max(locations map[int]string) int {
	max := -1
	for i := range locations {
		if i > max {
			max = i
		}
	}
	return max
}

func find_min(locations map[int]string) int {
	min := 100000
	for i := range locations {
		if i < min {
			min = i
		}
	}
	return min
}

func find_number(line string) int {
	digits := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}
	locations := make(map[int]string)

	for i := 0; i < len(line); i++ {
		for j := 1; j < 6; j++ {
			if i+j > len(line) {
				break
			}
			substring := line[i : i+j]
			if value, ok := digits[substring]; ok {
				locations[i] = value
				break
			} else if _, err := strconv.Atoi(substring); err == nil {
				locations[i] = substring
				break
			}
		}
	}

	number, _ := strconv.Atoi(locations[find_min(locations)] + locations[find_max(locations)])
	return number
}

func main() {
	file, _ := os.ReadFile("input.txt")

	total := 0
	for _, line := range strings.Split(string(file), "\n") {
		total += find_number(line)
	}

	fmt.Println(total)
}
