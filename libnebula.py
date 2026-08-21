from collections import defaultdict

# this file starts with only two classes: 
# InvertedIndex
# SearchResults


# Alternate Constructor decorators from section 8.16 in Python Cookbook 2013-Beazley
class InvertedIndex:
	# Primary Constructor
	def __init__(self):
		#self.index: defaultdict[str, dict[tuple[str, int], int]] = defaultdict(dict)
		self.index = defaultdict(lambda: defaultdict(int))
		# example self.index["treasure"][("1342", 57)] = 3
		# 1342 is the book and 57 is the line number because gutenberg does not have pages

	# Alternate Constructor/Loader
	@classmethod
	def from_docs(cls, docs):
		index = cls()
		
		for doc, text in docs.items():
			lines = text.splitlines()

			for line_number, line in enumerate(lines, start=1):
				words = line.split()

				for word in words:
					index.index[word][(doc, line_number)] += 1
		return index
	# Alternate Constructor/Loader
	@classmethod
	def from_save(cls, savefile):
		pass

	# Create Save File
	def save(self):
		pass
	def __str__(self):
		output = ""

		for word, occurrences in list(self.index.items())[:3]:
			output += f"{word}: {occurrences}\n"

		return output

class SearchResults:
	# Primary Constructor
	def __init__(self):
		self.results = {}
