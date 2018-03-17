#PE_Q3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#ToDo
#How to find if prime?

orig_num = 600851475143
num = 600851475143

fact_list = []
prime_list = []

def get_factors(num): #Takes a large number and returns factors
	for i in xrange(1, num):
		if num % i == 0:
			fact_list.append(i)
			#break
	return fact_list

def get_prime(num): #Takes a list of factors and returns their primality
	is_prime = False
	for j in num:
		prime_list.append(j)
		for i in xrange(2, j):
			if j % i == 0:
				is_prime = False
				break
			else:
				is_prime = True
		prime_list.append(is_prime)
	return prime_list

#print get_factors(num)
print get_prime(get_factors(num))
#print get_prime(get_factors(num))

# def get_prime(num):
# 	is_prime = False
# 	for i in xrange(2, num):
# 		if num % i == 0:
# 			is_prime = False
# 			break
# 		else:
# 			is_prime = True
# 	return is_prime
				