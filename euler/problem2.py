print("By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.")
limit = 4000000
sumeven = 2 # because i will begin the addition with 1 and 2 i must consider 2 now
swap = 0
fprev =1
factu = 2
while (factu <= limit):
  swap = factu
  factu = fprev + factu
  fprev = swap
  if(factu%2 == 0):
    sumeven += factu
print(sumeven)