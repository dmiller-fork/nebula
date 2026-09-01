import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).parent.parent))

from libnebula import InvertedIndex
from libnebula import SearchResults
from libnebula import TFIDFcalc
from libnebula import KRankHeap

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

	# now run triple for loop 
	book_scores = defaultdict(float)
	for term, books in search_results.results.items():
		df = len(books)
		idf = tfidf.calc_idf(df, tfidf.total_number_of_docs)
		## small optimization the query term "the" gets filtered out here
		## because "the" is in every document  log(total/total) -> log(1) = 0
		if idf == 0:
			continue
		for bookid, lines in books.items():
			term_count = sum(lines.values())
			tf = tfidf.calc_tf(term_count, tfidf.book_lengths[bookid])
			book_scores[bookid] += tf * idf
	# for bookid, score in book_scores.items():
		# print(bookid, score)
	k = 5 
	rank_heap = KRankHeap(k)

	for bookid, score in book_scores.items():
		rank_heap.add_result(bookid, score)
	print(rank_heap.list_results())
