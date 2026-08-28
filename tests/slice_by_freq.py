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
	index.slice_by_freq(50, 100)
	print(index.words_by_freq[-100:])

