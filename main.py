import math

memoizedValues = []

def performMethod(x):
  if x%2 == 0:
    return x/2
  else:
    return (3*x) + 1

def checkFound(x):
  if (x in memoizedValues) or (math.log(float(x), 2) == int(math.log(float(x), 2))):
    return True
  return False

limit = int(input('How many values do you want to check? '))

for i in range(1, limit + 1):
  orgVal = i
  currentVal = i
  isFound = False
  while True:
    if checkFound(currentVal):
      isFound = True
      break
    else:
      currentVal = performMethod(currentVal)
  if isFound:
    memoizedValues.append(orgVal)
  print('{}: {}'.format(orgVal, isFound))



  