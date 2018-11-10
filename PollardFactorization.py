#!/usr/bin/env python3

import math
import primefac
N = int(input("The number I want factored is: "))
a = int(input("set a to: "))

def powerMod(number,power):
	for pow in range(2,power+1):
		number = (number**pow) % N
	return number

def pollard(a,N):
	for j in range(2,100):
		a = powerMod(a,j)-1

		d = math.gcd(a,N)
		#print("at %d! a and d are: %d %d "%(j,a,d))
		if(d>1 and d<N):
			q = N//d

			#print("aha! at %d! I found the factors %d and %d "%(j,d,q))
			d = d-1
			pfactors = list(primefac.primefac(d-1))
			print("the prime factors of "+str(d-1)+" are: ")
			print(pfactors)

			q = q-1
			qfactors = list(primefac.primefac(q-1))
			print("the prime factors of "+str(q-1)+" are: ")
			print(qfactors)
			return True

pollard(a,N)