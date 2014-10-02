print("Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.")
sumofsquare = 0
sumnumber = 0

for i in range(1,100):
  sumofsquare += i*i #calculate the square of each number and add it to the sum
  sumnumber += i     #sum the 100 first number
squareofsum = sumnumber * sumnumber #get the square of the sum of the first 100 number
print("difference ")
print(squareofsum-sumofsquare)