def longest_consecutive(nums):
    current_seq = 0
    total_seq = 0

    for i in range(len(nums)):
        if nums[i + 1] == nums[i] + 1 and i != len(nums) - 1:
            current_seq += 1
        else:
            if current_seq > total_seq:
                total_seq = current_seq
            else:
                current_seq = 0
