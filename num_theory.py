# several number theory algorithms implemented in python
# for any particular use, authored by Neelam Akula 2021.

import os
import math

def isPrime(n):
  return all(n % i for i in range(2, n))

def factors(n):
  factors = []
  p = 2
  while True:
    while n % p == 0 and n > 0:
      factors.append(p)
      n = n/p
    p += 1
    if p > n / p:
      break
  if n > 1:
    factors.append(n)
  return factors

def euclidean(a, b):
  if a == 0:
    return b, 0, 1
  gcd, x1, y1 = euclidean(b%a, a)
  x = y1 - (b//a) * x1
  y = x1
  return gcd, x, y

def inverse(a,m):
  (gcd, b, x) = euclidean(a, m)
  if b < 0:
    b = (b % m + m) % m
  return b

def CRT(n1, r1, n2, r2):
  (gcd, x, y) = euclidean(n1, n2)
  m = n1 * n2
  n = r2 * x * n1 + r1 * y * n2
  return (n % m + m) % m

def isMersenne(n):
  M = 2**n - 1
  for k in range (1, int(math.sqrt(M))):
    factor = (2*n)*k + 1
    if M % factor == 0:
      print(M/factor)
      return False
  return True

def legendre(a, p):
  if isPrime(p):
    if a >= p or a < 0:
      return legendre(a%p, p)
    elif a == 0 or a == 1:
      return a
    elif a == 2:
      if p % 8 == 1 or p % 8 == 7:
        return 1
      else:
        return -1
    elif a == p - 1:
      if p % 4 == 1:
        return 1
      else:
        return -1
    elif not isPrime(a):
      factors = factors(a)
      prod = 1
      for p_i in factors:
        prod *= legendre(p_i, p)
        return prod
    else:
      if ((p-1)/2) % 2 == 0 or ((a-1)/2) % 2 == 0:
        return legendre(p, a)
      else:
         return (-1) * legendre(p, a)
  else:
    print("Error, p is not prime!")


def runner():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("=======================================")
  print("Select which program to run:")
  print("=======================================")
  print("Is Prime \t\t\t1")
  print("Factors \t\t\t2")
  print("Chinese Remainder Theorem \t3")
  print("Euclidean Algorithm \t\t4")
  print("Mersenne Prime \t\t\t5")
  print("Legendre \t\t\t6")
  print("Multiplicative Inverse \t\t7")
  print("=======================================")
  prog = input("Enter Program Here: ")
  if prog == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    n = input("Enter n for is prime: ")
    print(isPrime(n))
  elif prog == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    n = input("Enter n for prime factors: ")
    print(factors(n))
  elif prog == 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("CRT Format is as follows:")
    print("X is congruent to R1 mod N1")
    print("X is congruent to R2 mod N2")
    print("=======================================")
    n1 = input("Enter n1 for CRT: ")
    r1 = input("Enter r1 for CRT: ")
    n2 = input("Enter n2 for CRT: ")
    r2 = input("Enter r2 for CRT: ")
    print("X = " + str(CRT(n1, r1, n2, r2)))
  elif prog == 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    a = input("Enter a for Euclidean Algorithm: ")
    b = input("Enter b for Euclidean Algorithm: ")
    print(euclidean(a, b))
  elif prog == 5:
    os.system('cls' if os.name == 'nt' else 'clear')
    n = input("Enter n for is Mersenne Prime: ")
    print(isMersenne(n))
  elif prog == 6:
    os.system('cls' if os.name == 'nt' else 'clear')
    a = input("Enter a for Legendre Symbol: ")
    p = input("Enter p for Legendre Symbol: ")
    print(legendre(a, p))
  elif prog == 7:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("MI Format is as follows:")
    print("A*X is congruent to 1 mod M")
    print("=======================================")
    m = input("Enter m for Multiplicative Inverse: ")
    a = input("Enter a for Multiplicative Inverse: ")
    print("X = " + str(inverse(a, m)))
  else:
    print("Invalid Program")

if __name__ == "__main__":
  runner()

