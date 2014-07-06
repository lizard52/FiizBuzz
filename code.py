#For multiples of 3, print "Fizz"; multiples of 5, print "Buzz"; 
#and for both print "FizzBuzz"

def fizzbuzz(n): 
"""
Takes one parameter and returns "Fizz", "Buzz", "FizzBuzz", or n 
depending on the multiple.
"""
	if (n % 3 == 0 and n % 5 == 0):
		return 'FizzBuzz'
	elif n % 3 == 0:
		return 'Fizz'
	elif n % 5 == 0:
		return 'Buzz'
	else: 
		return n 

#empty list for storing results
numlist = [] 

#loops through 1 to 100 
for n in range(1, 101): 
#Uses the fizzbuzz function and 
#the results get appended to numlist
	numlist.append(fizzbuzz(n))  
	
#prints the results in an array
print numlist 

