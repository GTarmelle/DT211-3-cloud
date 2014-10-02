print("Find the largest palindrome made from the product of two 3-digit numbers.")
x = y = 999
largestp = 0
def ispalindrome(n): # use to examine if a giving number is a palindrome
  nToString = str(n)
  arglenght = len(nToString)
  argReverseLenght = arglenght -1
  for i in range(0,(arglenght -1)):
    if(nToString[i] != nToString[argReverseLenght]):
      return bool(0)
    else:
      argReverseLenght -= 1
    
  return bool(1)

#go throught all 3 digit numbers o find the largest palindrome
maxp = 0
while(x>0):
  while(y>0):
    largestp = x*y
    if(ispalindrome(largestp)):
      if(maxp < largestp):
        maxp = largestp
    y -=1
  x -=1
  y = 999
print(maxp)
    
    