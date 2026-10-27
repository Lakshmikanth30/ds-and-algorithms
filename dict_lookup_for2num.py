nums = [14, 3, 8, 21, 5, 11]
target = 16

lookup = {}
for index, number in enumerate(nums):
    current_diff = target - number
    if current_diff in lookup:
        print([lookup[current_diff], index])
        break
    lookup[number] = index