print("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?")
i = 2520 # if 2520 is the smallest number that can be divided 
         #by each of the numbers from 1 to 10 without any remainder
         #then there is no smallest number evenly divisible by all of the numbers from 1 to 20
myrange = [2520,11,12,13,14,15,16,17,18,19,20]    
def isdivided(n): #check if the number is evenly divisible by all of the numbers from 1 to 20
  for j in myrange:
    if((i%j)!=0):
      return bool(0)
  return bool(1)

notfound = bool(1)
while(notfound): #increment the number from 2520 till the number searched is found
  if(isdivided(i)):
    notfound = bool(0)
  else:
    i += 1
print(i)