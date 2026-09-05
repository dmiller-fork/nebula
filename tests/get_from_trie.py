import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from libnebula import Trie
trie = Trie()

print("inserting preprocess, processing, process")
trie.insert("preprocess")
trie.insert("processing")
trie.insert("process")

print("get list for stem: 'proce'")
print(trie.words_with_stem("proce"))
