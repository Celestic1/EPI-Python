'''
Given an array of integers, reorder the array so the even entries appear first

My solution
O(n) time
O(1) space

[1,2,3,8,4] = [2,8,4,1,3]
[2,1,3,8,4] = [2,8,4,1,3]
[4, 10, 6, 11, 15, 0, 16, 3, 18, 16, 18, 8, 12, 6, 14, 4, 9, 8, 8, 12, 12, 16, 22] = 
[4, 10, 6, 0, 16, 18, 16, 18, 8, 12, 6, 14, 4, 8, 8, 12, 12, 16, 22, 15, 9, 3, 11]
'''

def ordereven(nums):
  prev = 0
  for i in range(1,len(nums)):
    if not nums[prev]&1 and nums[i]&1:
      prev += 1
    elif nums[prev]&1 and not nums[i]&1:
      nums[prev],nums[i] = nums[i],nums[prev]
      prev += 1
    elif not nums[prev]&1 and not nums[i]&1:
      prev = i
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
