'''
[1,2,3] + [3,7,7] = [5,0,0]
Add two list and return the new list
'''

def add_one(A,B):
  carry = 0
  result = []
  short = lng = None
  A.reverse()
  B.reverse()

  if len(A) > len(B):
    short = B
    lng = A
  else:
    short = A
    lng = B
    
  for i in (range(len(short))):
    sum = A[i] + B[i] + carry
    if sum >= 10:
      carry = 1
    else:
      carry = 0
    result.append(sum%10)

  for num in (lng[len(B):]):
    sum = num + carry
    if sum == 10:
      carry = 1
    else:
      carry = 0
    result.append(sum%10)
  if carry == 1:
    result.append(1)
  result.reverse()
  return result
