package main

import "fmt"

func containsDuplicate(nums []int) bool {
    seen := map[int]bool{}

    for num := range(nums) {
        fmt.Print(num, seen[num])
        if ok := seen[num]; ok {
            return true
        }

        seen[num] = true
    }

    return false
}

func main() {
    containsDuplicate([]int{1, 2, 3, 1})
}
