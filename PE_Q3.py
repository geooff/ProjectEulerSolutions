#PE_Q3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#ToDo
#How to find if prime?

orig_num = 600851475143
num = 4000

sqt_num = int(num ** 0.5)
fact_list = []


def get_factors(num):
	for i in range(1, num):
		if num % i == 0:
			fact_list.append(i)
	return fact_list

print get_factors(num)

def get_prime_factores(factors):
	prime_fact_list = []
	for i in range(len(factors)):
		print fact_list(i)		
		#for j in range(get_factors(i)):
		#	if get_factors(i) % j == 0:
		#		prime_fact_list.append(get_factors(i))
	#return prime_fact_list

print get_prime_factores(get_factors(num))
				