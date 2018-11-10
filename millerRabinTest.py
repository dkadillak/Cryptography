#!/usr/bin/env python3

import random
import math
import numpy as np

primeCandidate = int(input("The number I want to check is a prime is: "))
#x = int(input("Compute the pi function pi(x) where x = "))+1

def powerOf2Factorization(primeCandidate):
	oddRemainder = primeCandidate
	oddRemainder-=1
	power = 0

	while(oddRemainder%2 != 1):
		if(oddRemainder%2 == 0):
			power+=1
			oddRemainder /= 2

	return power, int(oddRemainder)

def millerRabinTest(power, oddRemainder,primeCandidate):
	if(primeCandidate ==2):
		return True
	if(primeCandidate%2 == 0):
		return False

	for x in range (0,10):
		random_number = random.randint(2,primeCandidate-1)
		if(isWitness(power,oddRemainder,random_number,primeCandidate) == True):
			return False
		#print(str(random_number)+" was not a witness")

	return True


def isWitness(power, oddRemainder, a, n):
	a_copy = a
	gcd = math.gcd(a,n)
	if(gcd>1 and gcd <n):
		return False

	a = (a**oddRemainder) % n

	if(a == 1):
		return False

	for x in range(0,power):

		a = (a**2) %n
		if(a == -1 or a ==1):
			return False
	#print("Found MR witness: "+str(a_copy))
	return True 


power,oddRemainder = powerOf2Factorization(primeCandidate)
print(millerRabinTest(power,oddRemainder,primeCandidate))

'''
#problem number 3a
def calculateNumPrimes(val):
	num_of_primes = 0
	for val in range(2,x):
		power,oddRemainder = powerOf2Factorization(val)
		if(millerRabinTest(power,oddRemainder,val)):
			num_of_primes+=1
	return num_of_primes



#problem 3b
def calculateRatio():
	x =100
	for i in range(4):
		numerator = calculateNumPrimes(x)
		denominator = x/np.ln(x)
		print("ratio for x=%d is: "%(x,numerator/denominator))
		x*=10


'''













