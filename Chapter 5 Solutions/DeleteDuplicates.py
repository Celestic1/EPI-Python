'''
Takes in a sorted array
remove duplicates and 
shift remaining elements to the left
can't use built-in delete functions

[2,3,5,5,7] returns 4
and [2,3,5,5,7] becomes [2,3,5,7,5]
'''

def delete_duplicates(A):
  if not A:
    return 0

  curr = 1
  for i in range(1,(len(A))):
    print(curr,i)
    if A[curr-1] != A[i]:
      A[curr] = A[i]
      curr += 1
  return curr
