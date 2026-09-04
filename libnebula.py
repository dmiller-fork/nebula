import string
from collections import defaultdict
import heapq
import math

# this file starts with only two classes: 

## InvertedIndex
## SearchResults

# UPDATE adding two classes

## TFIDFcalc
## KRankHeap

# Last step the presenter

## RankedResults

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
	"""
	SearchResults is a projection of the inverted index
	that only includes the query terms.

	The tuple key is unpacked a three level dictionary:
	search_results.resultsterm][bookid][line] = count

	Note. This is a reference copy, so READ ONLY
	Do Not Modify search results or you will modify inverted index
	"""
	# Primary Constructor
	def __init__(self):
		self.results = defaultdict(
			lambda: defaultdict(
				lambda: defaultdict(int)
			)
		)

	# Alternate Constructor/Loader
	@classmethod
	def query_index(cls, index, query):
		results = cls()
		query_words = query.split()
		for word in query_words:
			word = word.strip(PUNCTUATION).lower()
			if word in index.index:
				for (bookid, line_number), count in index.index[word].items():
					results.results[word][bookid][line_number] = count
		return results

class TFIDFcalc:
	""" this class is necessary because
		there are many definitions of term frequency tf
		and inverse document frequency idf.
		in the def below tf is normalized by doc_length
		and idf is a log calculation log(N/n),
		where N is total number of docs, and
		n is number of docs in which query term t_k occurs,
		where k is an iterator for each query term.
	"""
	def __init__(self, books):
		self.book_lengths = {
			bookid: len(text.split())
			for bookid, text in books.items()
		}
		self.total_number_of_docs = len(books)

	@staticmethod
	def calc_tf(freq_of_term, doc_length):
		return freq_of_term / doc_length 

	@staticmethod
	def calc_idf(number_of_docs_w_term, total_number_of_docs):
		return math.log(total_number_of_docs / number_of_docs_w_term)



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

class RankedResults:
	""" This class compiles search results and rank_scores into 
	score_list->books_dict->list of tuples (term, line, count)
	
	Note. This is a reference copy, so READ ONLY
	Do Not Modify Ranked results or you will modify inverted index
	"""
	def __init__(self, search_results, rank_scores):
		self.ranked_results = []
		self.snippets = []
		for score, book in rank_scores:
			results = []

			for term in search_results:
				if book in search_results[term]:
					for line, count in search_results[term][book].items():
						results.append((term, line, count))
			results.sort(key=lambda x: x[1]) #sorts tuples by line number
			self.ranked_results.append({book: results})

	def getSnippetStarts(self, window_size, terms):
		for book_dict in self.ranked_results:
			for book, results in book_dict.items():

				highest_count = 0
				highest_starting_line_tuple = (0, 0, 0)

				for i, (term, line, count) in enumerate(results):
					if term in terms:
						start_tuple = (term, line, count)
						start_line = line
						window_count = 0

						for term, line, count in results[i:]:
							if line > start_line + window_size:
								break

							if term in terms:
								window_count += count

						if window_count > highest_count:
							highest_count = window_count
							highest_starting_line_tuple = start_tuple
			book_dict[book] = highest_starting_line_tuple
			book = highest_starting_line_tuple
		
	def generateSnippets(self, books, window_size):

		for book_dict in self.ranked_results:
			for book, start_tuple in book_dict.items():

				if start_tuple == (0, 0, 0):
					self.snippets.append({
						book: "no snippets found"
					})
					continue

				start_line = start_tuple[1]
				lines = books[book].splitlines()
				snippet = lines[start_line - 1:start_line - 1 + window_size]

				self.snippets.append({
					book: "\n".join(snippet)
				})
	@staticmethod
	def get_title(book_text):
		lines = book_text.splitlines()
		for line in lines:
			if line.startswith("Title:"):
				return line.removeprefix("Title:").strip()
