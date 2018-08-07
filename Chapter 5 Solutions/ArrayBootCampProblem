'''
Given an array of integers, reorder the array so the even entries appear first

My solution
O(n) time
O(1) space

[1,2,3,8,4] = [2,8,4,1,3]
[2,1,3,8,4] = [2,8,4,1,3]
'''

def ordereven(nums):
  prev = 0
  for i in range(1,len(nums)):
    if not nums[prev]&1 and nums[i]&1:
      prev += 1
    elif nums[prev]&1 and not nums[i]&1:
      nums[prev],nums[i] = nums[i],nums[prev]
      prev += 1
  return nums
  
'''
book solution
O(n) time
O(1) space
'''

def even_odd(A):
  next_even, next_odd = 0, len(A) - 1
  while next_even < next_odd:
    if A[next_even] % 2 == 0:
      next_even += 1
    else:
      A[next_even], A[next_odd] = A[next_odd], A[next_even]
      next_odd -= 1
  return A
