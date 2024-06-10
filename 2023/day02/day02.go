package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func get_draws(line string) [][]string {
	var draws [][]string

	for _, draw := range strings.Split(strings.Split(line, ":")[1], ";") {
		var draw_list []string
		for _, count := range strings.Split(draw, ", ") {
			draw_list = append(draw_list, strings.ReplaceAll(strings.TrimSpace(count), "\n", ""))
		}
		draws = append(draws, draw_list)
	}

	return draws
}

func get_maximum_color_counts(draws [][]string) []int {
	maximum_values := map[string]int{
		"red":   0,
		"green": 0,
		"blue":  0,
	}

	for _, draw := range draws {
		for _, count := range draw {
			split_count := strings.Split(string(count), " ")
			value, _ := strconv.Atoi(split_count[0])
			color := split_count[1]

			if value > maximum_values[color] {
				maximum_values[color] = value
			}
		}
	}

	var values []int
	for _, value := range maximum_values {
		values = append(values, value)
	}

	return values
}

func get_product(counts []int) int {
	product := 1
	for _, number := range counts {
		product *= number
	}
	return product
}

func main() {
	file, _ := os.ReadFile("input.txt")

	total := 0
	for _, line := range strings.Split(string(file), "\n") {
		total += get_product(get_maximum_color_counts(get_draws(strings.TrimSpace(line))))
	}

	fmt.Println(total)
}
