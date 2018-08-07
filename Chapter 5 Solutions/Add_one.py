'''
Add one to an array of digits representing 
a number and return the corresponding array
[1,2,9] + 1 = [1,3,0]

O(n) time
O(n) space
'''

def add_one(A):
  carry = 1
  result = []
  for i in reversed(range(len(A))):
    sum = A[i] + carry
    if sum == 10:
      carry = 1
    else:
      carry = 0
    result.append(sum%10)
  if carry == 1:
    result.append(1)
  return list(reversed(result))
