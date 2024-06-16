package main

import (
	"fmt"
	"os"
	"strings"
)

func pop(s *[]int) int {
	element := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return element
}

func contains(slice []string, target string) bool {
	for _, element := range slice {
		if element == target {
			return true
		}
	}
	return false
}

func get_card_win_count(numbers []string) int {
	winning_numbers := strings.Fields(numbers[0])
	card_numbers := strings.Fields(numbers[1])
	count := 0

	for _, number := range card_numbers {
		if contains(winning_numbers, number) {
			count += 1
		}
	}

	return count
}

func get_card_win_counts_and_queue(data []string) (map[int]int, []int) {
	card_win_counts := make(map[int]int)
	var queue []int

	for i, line := range data {
		numbers := strings.Split(strings.Split(strings.TrimSpace(line), ":")[1], "|")
		card_win_counts[i] = get_card_win_count(numbers)
		queue = append(queue, i)
	}

	return card_win_counts, queue
}

func get_total_number_of_cards(card_win_counts map[int]int, queue []int) int {
	total := 0

	for len(queue) > 0 {
		total += 1
		i := pop(&queue)

		for j := i + 1; j < i+card_win_counts[i]+1; j++ {
			queue = append(queue, j)
		}
	}

	return total
}

func main() {
	raw_data, _ := os.ReadFile("input.txt")
	data := strings.Split(string(raw_data), "\n")

	card_win_counts, queue := get_card_win_counts_and_queue(data)
	total_number_of_cards := get_total_number_of_cards(card_win_counts, queue)

	fmt.Println(total_number_of_cards)
}
