# Given an array of characters, write a method to replace all the spaces with “&32”.
# You may assume that the array has sufficient slots at the end to hold the additional
# characters, and that you are given the “true” length of the array. (Please perform this
# operation in place with no other auxiliary structure).


def replaceBlankSpaces(string, size):
	"""Replace all the spaces with &32"""
	
	#Remove the first and last blank space
	string = string.strip()
	l  = len(string)

	#Verify the real size with input size
	if l == size:	
		#Count blank spaces
		blank_spaces = string.count(' ')		
		
		#Find new size
		new_size = size + (blank_spaces * 2)
		string = list(string)
		aux = new_size - 1

		#Fill the list with "*" character
		for i in range(size - 2, new_size - 2):		
			string.append('*')

		for j in range (size-1, 0, -1):
			#Replace blank space from the last
			if string[j] == ' ':
				string[aux] = '2'
				string[aux - 1] = '3'
				string[aux - 2] = '&'
				aux = aux - 3
			else:
				string[aux] = string[j]
				aux = aux - 1
		return ''.join(string)
	else:
		return "The size is wrong"

if __name__ == '__main__':
	text = "User is not allowed"
	text = replaceBlankSpaces(text,19)
	print (text)

"""
The algorithm complexity is O(n), because it looks for a blank space in the string to replace by "&32. 
The space complexity of this algorithm depends of amount of blank spaces or the string length. 
"""
