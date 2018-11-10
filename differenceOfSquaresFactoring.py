#!/usr/bin/env python3

import math

N = int(input("Factor this number: "))

b = 1
while True:
	possibleSquare = N+(b**2)
	sqrt = int(math.sqrt(possibleSquare))

	print("possibleSquare at b = {} is: {}".format(b,possibleSquare))
	print("sqrt is: {}".format(sqrt))

	'''
	to avoid comparing floating point numbers, I floored the
	result of the square root and will return true only if the floored sqrt^2 = the possibleSquare
	
	'''
	if((sqrt**2) == possibleSquare):
		print("found a square! {}+{}^2 = {}^2".format(N,b,sqrt))
		break
	b+=1


