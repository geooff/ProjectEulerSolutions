#PE_Q1
#Find the sum of all the multiples of 3 or 5 below 1000

#make list of multiples of 3
#make list of multiples of 5
#need i%3 U i%5
#sum lists


total = 0
listx = []
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		listx.append(i)

for i in listx:
	total += i

print total
