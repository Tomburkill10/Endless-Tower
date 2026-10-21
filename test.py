nums = [1,3,2,5]
output = []
if nums.count(0) >= 2:
    output = [0] * len(nums)
if nums.count(0) == 1:
    output = [0] * len(nums)
    zero_index = nums.index(0)
    prefix = nums[:zero_index]
    suffix = nums[zero_index + 1:]
    product = 1
    for num in prefix:
        product = product * num
    for num in suffix:
        product = product * num
    output[]
else:
    product = 1
    for num in nums:
        product = product * num
    for num in nums:
        output.append(product / num)
print(output)








