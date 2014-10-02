print("What is the 10 001st prime number?")
count = 6 # 13 is the 6th prime number, so i will begin with 14

def isprime(x): #check if a giving number is prime
  for y in range (2,x):
    if(x%y ==0):
      return bool(0)
  return bool(1)

res = 0
i = 14
while(count < 1000):
  if(isprime(i)):
    count +=1
    res = i
  i += 1
print(res)