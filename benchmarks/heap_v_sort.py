import sys
from pathlib import Path
from collections import defaultdict
import time

sys.path.append(str(Path(__file__).parent.parent))

from libnebula import InvertedIndex
from libnebula import SearchResults
from libnebula import TFIDFcalc
from libnebula import KRankHeap
from libnebula import RankedResults

books = {}
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "gutenberg"

for file in DATA_DIR.glob("*.txt"):
	books[file.stem] = file.read_text()

if __name__ == "__main__":
	index = InvertedIndex.from_docs(books)
	query = "treasure the"
	print("query is two terms:", query)
	search_results = SearchResults.query_index(index, query);
	# print(search_results.results)
	# tfidf object creates doc_lengths and total_number_of_docs
	tfidf = TFIDFcalc(books) # this gives setup for doc_word_count

	# now run for loops
	book_scores = defaultdict(float)
	for term, book_postings in search_results.results.items():
		df = len(book_postings)
		idf = tfidf.calc_idf(df, tfidf.total_number_of_docs)
		## small optimization
		if idf == 0:
			continue
		for bookid, lines in book_postings.items():
			term_count = sum(lines.values())
			tf = tfidf.calc_tf(term_count, tfidf.book_lengths[bookid])
			book_scores[bookid] += tf * idf
	# scoring/heap logic
	def heap_rank(book_scores, k):
		rank_heap = KRankHeap(k)

		for bookid, score in book_scores.items():
			rank_heap.add_result(bookid, score)

		return rank_heap


	def sort_rank(book_scores, k):
		ranked = sorted(
			book_scores.items(),
			key=lambda x: x[1],
			reverse=True
		)

		return ranked[:k]


	start = time.perf_counter()
	heap_rank(book_scores, 2)
	heap_time = time.perf_counter() - start

	start = time.perf_counter()
	sort_rank(book_scores, 2)
	sort_time = time.perf_counter() - start

	print(f"Heap: {heap_time:.6f} seconds")
	print(f"Sort: {sort_time:.6f} seconds")
	
