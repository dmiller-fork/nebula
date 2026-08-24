import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from libnebula import InvertedIndex
from libnebula import SearchResults
"""
books = {
    "test": "the the the\nfoo the\nbar"
}
"""

books = {}
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "gutenberg"

for file in DATA_DIR.glob("*.txt"):
	books[file.stem] = file.read_text()

if __name__ == "__main__":
	index = InvertedIndex.from_docs(books)
	print("index size:", len(index.index))
	#print(index)
	query = "treasure Jim"
	search_results = SearchResults.query_index(index, query);
	print(search_results.results);

# compare the above results to the result below. Make some design decisions:
# for example "treasure," is not found in the current implementation
"""
 grep -n "treasure" 84.txt
935:treasures known to few besides myself. I have described myself as always
3845:a treasure which would fully reward his toil and hazard.
4010:possession of these treasures gave me extreme delight; I now continually
4154:never driven away. I asked, it is true, for greater treasures than a
6176:Elizabeth I possessed a treasure, alas, balanced by those horrors of
"""
