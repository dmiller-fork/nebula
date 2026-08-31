import string
from collections import defaultdict
import heapq
import math

# this file starts with only two classes: 

# InvertedIndex
# SearchResults

# UPDATE adding two classes
# TFIDFcalc
# KRankHeap

# GLOBALS
PUNCTUATION = string.punctuation + "“”‘’"

# Alternate Constructor decorators from section 8.16 in Python Cookbook 2013-Beazley
class InvertedIndex:
	# Primary Constructor
	def __init__(self):
		#self.index: defaultdict[str, dict[tuple[str, int], int]] = defaultdict(dict)
		# example self.index["treasure"][("1342", 57)] = 3
		# 1342 is the book and 57 is the line number because gutenberg does not have pages
		self.index = defaultdict(lambda: defaultdict(int))
		self.words_by_freq = None
		# words_by_freq is a list of the keys sorted by frequency
		# we can use this list to slice up the inverted index

	# Alternate Constructor/Loader
	@classmethod
	def from_docs(cls, docs):
		index = cls()
	
		for doc, text in docs.items():
			lines = text.splitlines()

			for line_number, line in enumerate(lines, start=1):
				words = line.split()

				for word in words:
					word = word.strip(PUNCTUATION).lower()
					index.index[word][(doc, line_number)] += 1
		return index
	# Alternate Constructor/Loader
	@classmethod
	def from_save(cls, savefile):
		pass 

	# Create Save File
	def save(self):
		pass

	# the follwing is three methods gen_words_by_freq, slice, and filter
	# these methods all you to shrink the index by word count
	# a cool test is keeping only medium to high freq words slice(35-85)
	# this cuts the index size in half, while still retaining most searched words
	def generate_words_by_freq(self):
		self.words_by_freq = sorted(
			self.index,
			key=lambda word: sum(self.index[word].values()),
			reverse=True
		)

	def slice_by_freq(self, start_percent, end_percent):
		start = int(len(self.words_by_freq) * start_percent / 100)
		end = int(len(self.words_by_freq) * end_percent / 100)
		self.words_by_freq = self.words_by_freq[start:end]

	def filter_by_freq(self):
		self.index = {word: self.index[word] for word in self.words_by_freq}
    
	def __str__(self):
		output = ""

		for word, occurrences in list(self.index.items())[:3]:
			output += f"{word}: {occurrences}\n"

		return output

class SearchResults:
	# Primary Constructor
	def __init__(self):
		self.results = defaultdict(lambda: defaultdict(int))

	# Alternate Constructor/Loader
	@classmethod
	def query_index(cls, index, query):
		results = cls()
		query_words = query.split()
		for word in query_words:
			word = word.strip(PUNCTUATION).lower()
			if word in index.index:
				for (document, position), count in index.index[word].items():
					results.results[document][word] += count
		return results

class TFIDFcalc:
	def __init__(self, books):
		self.doc_word_count = {
			book: len(text.split())
			for book, text in books.items()
		}
	@staticmethod
	def calc_tf(doc_term_count, doc_word_count):
		return doc_term_count / doc_word_count

	@staticmethod
	def calc_idf(corpus_size, results_size):
		return math.log(corpus_size / results_size)

"""
class KRankHeap:
	def __init__(self, k):
		self.k = k
		self.heap = []

	def add_result(self, item, rank):
		entry = (rank, item)

		if len(self.heap) < self.k:
			heapq.heappush(self.heap, entry)
		elif rank > self.heap[0][0]:
			heapq.heapreplace(self.heap, entry)

	def list_results(self):
		return sorted(self.heap, reverse=True)
"""
