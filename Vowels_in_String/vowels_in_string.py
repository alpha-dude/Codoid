# Using dictionary method we can use vowel letters as keys and count as values
def check(string, vowels):
	
	# casefold has been used to ignore cases
	string = string.casefold()
	
	# Forms a dictionary with key as a vowel
	# and the value as 0
	count = {}.fromkeys(vowels, 0)
	
	# To count the vowels
	for character in string:
		if character in count:
			count[character] += 1
	return count
	
# Main code
vowels = 'aeiouAEIOU'
string = "Code teaches you how to face really big problems" # Your sentence goes here
print (check(string, vowels))
