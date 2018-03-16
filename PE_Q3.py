#PE_Q3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#ToDo
#How to find if prime?

orig_num = 600851475143
num = 4000

sqt_num = int(num ** 0.5)

def get_factors(num):
	fact_list = []
	for i in range(1, num):
		if num % i == 0:
			fact_list.append(i)
	return fact_list

print get_factors(num)