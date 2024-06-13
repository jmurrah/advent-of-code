package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

type Tuple struct {
	X int
	Y int
	Z int
}

func get_sum(numbers []int) int {
	total := 0
	for _, number := range numbers {
		total += number
	}
	return total
}

func get_adjacent_numbers(data []string, indicies []Tuple) []Tuple {
	adjacent_numbers := make([]Tuple, 0)
	seen := make(map[Tuple]bool)

	for _, index := range indicies {
		i, j := index.X, index.Y
		for j >= 0 && j < len(data[i]) && unicode.IsDigit(rune(data[i][j])) {
			j -= 1
		}
		j += 1

		str_number, start := "", j
		for unicode.IsDigit(rune(data[i][j])) {
			str_number += string(data[i][j])
			j += 1
		}

		number, _ := strconv.Atoi(str_number)
		number_tuple := Tuple{X: start, Y: j, Z: number}

		if _, ok := seen[number_tuple]; !ok {
			adjacent_numbers = append(adjacent_numbers, number_tuple)
			seen[number_tuple] = true
		}
	}

	return adjacent_numbers
}

func get_adjacent_digit_indicies(data []string, x int, y int) []Tuple {
	var indicies []Tuple

	for i := x - 1; i <= x+1; i++ {
		for j := y - 1; j <= y+1; j++ {
			if x+i >= 0 && x+i < len(data) && y+j >= 0 && y+j < len(data[i]) && unicode.IsDigit(rune(data[x+i][y+j])) {
				indicies = append(indicies, Tuple{X: x + i, Y: y + j})
			}
		}
	}

	return indicies
}

func main() {
	raw_data, _ := os.ReadFile("input.txt")
	data := strings.Split(string(raw_data), "\n")

	var numbers []int

	for i, line := range data {
		for j, character := range line {
			if string(character) == "*" {
				adjacent_numbers := get_adjacent_numbers(data, get_adjacent_digit_indicies(data, i, j))
				if len(adjacent_numbers) == 2 {
					numbers = append(numbers, adjacent_numbers[0].Z*adjacent_numbers[1].Z)
				}

			}
		}
	}

	fmt.Println(get_sum(numbers))
}
