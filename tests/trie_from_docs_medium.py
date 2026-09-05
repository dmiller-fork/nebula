import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).parent.parent))

from libnebula import InvertedIndex
from libnebula import Trie


books = {}
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "gutenberg"

for file in DATA_DIR.glob("*.txt"):
	books[file.stem] = file.read_text()

if __name__ == "__main__":
	#index = InvertedIndex.from_docs(books)
	trie = Trie.from_docs(books)

	print("get list for stem: 'trea'")
	print(trie.words_with_stem("trea"))
