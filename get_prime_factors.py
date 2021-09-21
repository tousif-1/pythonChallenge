def get_prime_factors(N):
  factors = list()
  divisor = 2
  while(divisor <= N):
    if (N % divisor) == 0:
      factors.append(divisor)
      N = N/divisor
    else:
      divisor += 1
  return factors

fact = input("Enter your number to get Prime Factors: ")
result = get_prime_factors(int(fact))
print (result)
