#True Ones, False Zeros
#Create a function which returns a list of booleans, from a given number. 
#Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.

def integer_boolean(n):
	return [True if int(num) else False for num in n]

print(integer_boolean("00"))
print(integer_boolean("111"))
print(integer_boolean("10101"))

#Examples
#integer_boolean("100101") ➞ [True, False, False, True, False, True]
#integer_boolean("10") ➞ [True, False]
#integer_boolean("001") ➞ [False, False, True]

#Notes
#Expect numbers with 0 and 1 only.