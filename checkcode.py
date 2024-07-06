from collections import deque

def rotate_list(nums, k):
  for _ in range(k):
    nums.insert(0, nums.pop())
    print(nums)
  return nums





def rotate_list2(nums, k):
  d = deque(nums)  
  d.rotate(k)     
  return list(d)  


nums = [1,2,3,4,5]
k = 3

#print(rotate_list2(nums, k))


numbers = [1, 2, 3, 4, 5, 6, 7, 7, 9]

def removeOdd(nums):
    # Iterate through the list in reverse
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] % 2 != 0:  # Check for odd numbers
            del numbers[i]      # Remove the odd number

    return nums

print(removeOdd(numbers))  # Output: [2, 4, 6, 8]



