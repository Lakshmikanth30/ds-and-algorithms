nums = [14, 3, 8, 21, 5, 11]
target = 16

arr = sorted(enumerate(nums), key=lambda x: x[1])
left, right = 0, len(arr) - 1

while left < right:
    current_sum = arr[left][1] + arr[right][1]
    if current_sum > target:
        right -= 1
    elif current_sum < target:
        left += 1
    else:
        print([arr[left][0], arr[right][0]])
        break