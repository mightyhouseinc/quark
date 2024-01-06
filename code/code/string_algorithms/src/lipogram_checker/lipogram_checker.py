'''
A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once.
The best-known English pangram is "The quick brown fox jumps over the lazy dog."
A pangrammatic lipogram is a text that uses every letter of the alphabet but excludes one of them. 
'''
#Part of Cosmos by OpenGenus Foundation 
#
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def pangrammaticChecker(string):
	string.lower()
	counter = sum(1 for x in alphabet if (string.find(x)<0))
	if counter == 0:
		return "Pangram"
	elif counter == 1:
		return "Pangrammatic Lipogram"
	else:
		return "Not a pangram but might a lipogram"
if __name__ == '__main__':
	print(pangrammaticChecker("The quick brown fox jumps over the lazy dog"))