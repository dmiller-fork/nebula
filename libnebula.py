# this file starts with only two classes: 
# InvertedIndex
# SearchResults


# Alternate Constructor decorators from section 8.16 in Python Cookbook 2013-Beazley
class InvertedIndex:
	# Primary Constructor
	def __init__(self):
		self.index: dict[str, dict[tuple[str, int], int]] = {}

	# Alternate Constructor/Loader
	@classmethod
	def from_documents(cls, documents):
		pass

	# Alternate Constructor/Loader
	@classmethod
	def from_save(cls, savefile):
		pass

	# Create Save File
	def save(self):
		pass

class SearchResults:
	# Primary Constructor
	def __init__(self):
		self.results = {}
