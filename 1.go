package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var result []int
	counter := map[int]int{}

	for i := range len(nums) {
        fmt.Println(nums[i], target - nums[i], counter[target-nums[i]])
		if counter[target-nums[i]] != 0 {
			result = []int{i, counter[target-nums[i]] - 1}
            break
		}

		counter[nums[i]] = i + 1
	}

	return result
}

func main() {
    result := twoSum([]int{2, 7, 11, 15}, 9)

    fmt.Println(result)
}
