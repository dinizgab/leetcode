package main

func maxProfit(prices []int) int {
	j := 0
	profit := 0

	for i := range len(prices) {
		if i != j && prices[j] > prices[i] {
			j = i
		} else {
			actualProfit := prices[i] - prices[j]

			if actualProfit > profit {
				profit = actualProfit
			}
		}
	}

	return profit
}

func main() {
	maxProfit([]int{7, 5, 3, 6, 4})       // 3
	maxProfit([]int{7, 1, 5, 3, 6, 4})    // 5
	maxProfit([]int{2, 1, 2, 1, 0, 1, 2}) // 2
	maxProfit([]int{7, 6, 4, 3, 1})       // 0
}
