package main

import "fmt"

func countStudents(students []int, sandwiches []int) int {
	// We can use any length, since len(students) == len(sandwiches) always
	for range len(students) {
		for range len(sandwiches) {
			if students[0] == sandwiches[0] {
				sandwiches = sandwiches[1:]
				students = students[1:]
			} else {
				students = shiftLeft(students)
			}
		}
	}

	return len(students)
}

func shiftLeft(arr []int) []int {
	first := arr[0]

	for i := range len(arr) - 1 {
		arr[i] = arr[i+1]
	}

	arr[len(arr)-1] = first

	return arr
}

func main() {
	result := countStudents([]int{0}, []int{0})

	fmt.Println(result)
}

// sandwiches == stack (top == 0)
// students == queue (front == 0)

// If the sandwiches in front of the queue prefers
// the sandwiches in top of the stack, it will take it and leave the queue
// Otherwise it will go to the end of the queue

// This cycle continues until none of the students likes the
// type of the sandwiche at the top

// Count the number of students that are unable to eat
