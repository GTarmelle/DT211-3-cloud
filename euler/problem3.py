print("What is the largest prime factor of the number 600851475143 ?")
n = 600851475143
i = 2
largestPrime = 0
def isprime(x): #check if a giving number is prime
  for y in range (2,x):
    if(x%y ==0):
      return bool(0)
  return bool(1)

while(i<n):
  if((n%i)==0): #it's a factor of n
    if(isprime(i)) : #factor is prime
      if(largestPrime < i):
        largestPrime = i
  i +=1
print(largestPrime)
        