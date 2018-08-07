'''
Given an array of n nonnegative integers where A[i] 
denotes maximum distance you can advance from index i,
return whether it is possible to advance to the last index starting
from beginning of array

[3,3,1,0,2,0,1] = True
[3,2,0,0,2,0,1] = False
'''

def can_reach_end(A):
  last_index = len(A)-1
  curr = i = 0
  while i <= curr and curr < last_index:
    curr = max(curr,i+A[i])
    i += 1

  if curr >= last_index:
    return True
  return False
