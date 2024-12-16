package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.ReadFile("input.txt")
	safeCount := 0

	for _, line := range strings.Split(string(file), "\n") {
		record := strings.Split(line, " ")

		for i := range record {
			var smallerRecord []string
			smallerRecord = append(smallerRecord, record[:i]...)
			smallerRecord = append(smallerRecord, record[i+1:]...)

			prev, _ := strconv.Atoi(smallerRecord[0])
			first, isDecreasing, safe := true, true, true

			for _, strNum := range smallerRecord[1:] {
				num, _ := strconv.Atoi(strNum)
				difference := int(math.Abs(float64((prev - num))))

				if first {
					first = false
					if num > prev {
						isDecreasing = false
					}
				}

				if !(1 <= difference && difference <= 3) || (num > prev && isDecreasing) || (num < prev && !isDecreasing) {
					safe = false
					break
				}

				prev = num
			}

			if safe {
				safeCount += 1
				break
			}
		}
	}

	fmt.Println(safeCount)
}
