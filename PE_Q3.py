#PE_Q3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

orig_num = 600851475143
a = 600851475143
b = 2
c = 0

def get_prime_factor(a, b, c): #Takes a large number and returns factors
	print "Start"
	print "The current Largest devisor is: ",  c
	print "The current number we are trying to factor is: ", a
	while b < a/2:
		if a % b != 0:
			b += 1
		elif a % b == 0:
			c = b
			a = a / b
			if b > c:
				c = b
			b = 2
			print "The current Largest devisor is: ",  c
			print "The current number we are trying to factor is: ", a
	print a
	return "Finished!"

print get_prime_factor(a, b, c)
