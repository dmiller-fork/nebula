import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from libnebula import InvertedIndex
from libnebula import SearchResults
from libnebula import TFIDFcalc
books = {
    "test": "the the the\nfoo the\nbar",
	"foo": "the boo is a foo\nbar",
	"bar": "treasure is here"
}

# books = {}
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "gutenberg"

# for file in DATA_DIR.glob("*.txt"):
#	books[file.stem] = file.read_text()

if __name__ == "__main__":
	index = InvertedIndex.from_docs(books)
	query = "treasure Jim"
	search_results = SearchResults.query_index(index, query);
	# 4 parameters: 
	# doc_word_count, doc_term_count
	# corpus_size, search_results_size
	corpus_size = len(books)

	tfidf = TFIDFcalc(books) # this gives setup for doc_word_count
	for book, terms in search_results.results.items():
		book_score = 0

		for term, term_count in terms.items():
			doc_word_count = tfidf.doc_word_count[book]

			tf = tfidf.calc_tf(term_count, doc_word_count)

			term_results_size = len({doc for doc, line in index.index[term]})
			idf = tfidf.calc_idf(corpus_size, term_results_size)

			book_score += tf * idf

		print(book, book_score)
