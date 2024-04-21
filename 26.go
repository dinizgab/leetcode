package main

func removeDuplicates(nums []int) int {
    unique := 0

    for i := 0; i < len(nums); i++ {

        if nums[i] != nums[unique] {
            unique++
            nums[unique] = nums[i]
        }
    }

    unique++

    return unique
}

func main() {
    //removeDuplicates([]int{0,0,1,1,1,2,2,3,3,4})
    removeDuplicates([]int{1, 1, 2})
}
