package main

import "fmt"

func timeRequiredToBuy(tickets []int, k int) int {
	time := 0

	for i := range len(tickets) {
		if i > k {
            // We're using tickets[k] - 1 because we only need to pass
            // k - 1 times in the values in the Kth element
			time += min(tickets[i], tickets[k] - 1)
		} else {
			time += min(tickets[i], tickets[k])
		}
		fmt.Println(min(tickets[i], tickets[k]-1), time)
	}

	return time
}

func main() {
	fmt.Println(timeRequiredToBuy([]int{2, 3, 2, 1, 2}, 2))
	fmt.Println(timeRequiredToBuy([]int{84, 49, 5, 24, 70, 77, 87, 8}, 3))
}

// N people in a QUEUE, 0th is the start of it
// Tickets if the number of thickets that the Ith person want to buy
// Person buy one ticket and go to the final of the queue
// When a person has no tickets left to buy, remove from the queue
// Return the time that the person at K finished to buy all tickets
