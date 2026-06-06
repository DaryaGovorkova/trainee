def longest_increasing_streak(nums: list[int]) -> dict:

    max_start = 0
    max_length = 1

    current_start = 0
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_start = current_start
        else:
            # Последовательность прервалась, начинает новую с текущего элемента
            current_start = i
            current_length = 1

    if max_length <= 1:
        return {"length": 0, "streak": []}

    return {"length": max_length, "streak": nums[max_start: max_start + max_length]}


print(longest_increasing_streak([4,6,7,8,2,3,4,5]))