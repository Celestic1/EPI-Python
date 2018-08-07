'''
Given two lists as numbers, return the product of the two list in a list
'''

def multiply(A,B):
  sign = 0
  if A[0] < 0 and B[0] < 0 or A[0] > 0 and B[0] > 0:
    sign = 1
  else:
    sign = -1
  A[0],B[0]=abs(A[0]),abs(B[0])
  
  result = [0] * (len(A)+(len(B)))
  for i in reversed(range(len(A))):
    for j in reversed(range(len(B))):
      result[i+j+1] += A[i]*B[j]
      result[i+j] += result[i+j+1] // 10 
      result[i+j+1] %= 10
      
  return [result[0]*sign] + result[1:]
