nums = [34,56,23,42,9,21]
print(nums)
for i in range(len(nums)-1):
    min = i
    for j in range(i+1, len(nums)):
        if nums[j]<nums[min]:
           min = j
    temp = nums[min]
    nums[min] = nums[i]
    nums[i] = temp
    print(nums)


