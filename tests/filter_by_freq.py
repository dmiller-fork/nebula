import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from libnebula import InvertedIndex
from libnebula import SearchResults

books = {}
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "gutenberg"

for file in DATA_DIR.glob("*.txt"):
	books[file.stem] = file.read_text()

if __name__ == "__main__":
	index = InvertedIndex.from_docs(books)
	print("index size:", len(index.index))
	index.generate_words_by_freq()
	index.slice_by_freq(35, 85)
	index.filter_by_freq()
	print(index.words_by_freq[0:20])
	print("index size:", len(index.index))
	query = "disclose"
	search_results = SearchResults.query_index(index, query)
	print(search_results.results);
