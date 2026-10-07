'''nums = [12,35,1,10,34,1]
def second_largest(nums):

    nums.sort()
    n= len(nums)

    return nums[n-2]
print(second_largest(nums))'''

'''nums = [12,35,1,10,34,1]
def second_largest(nums):
    largest = float("-inf")
    S_largest = float("-inf")
    n=len(nums)
    for i in range(0,n):
        if nums[i]>largest:
            S_largest = largest
            largest = nums[i]
        elif nums[i]>S_largest and nums[i] != largest:
            S_largest = nums[i]
    return S_largest
print(second_largest(nums))'''

nums = [12,35,1,10,34,1]
def second_largest(nums):
    largest = float("-inf")
    S_largest = float("-inf")
    n = len(nums)
    for i in range (0,n):
        largest = max(largest,nums[i])
    for i in range(0,n):
        if nums[i]>S_largest and nums[i] != largest:
            S_largest=nums[i]
    return S_largest
print(second_largest(nums))
    
            
        
