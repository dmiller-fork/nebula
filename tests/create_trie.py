import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from libnebula import Trie
trie = Trie()

print("inserting preprocess, processing, process")
trie.insert("preprocess")
trie.insert("processing")
trie.insert("process")

print("check if process is in trie: should be true")
print(trie.contains("process"))     # True
print("check if processor is in trie: should be false")
print(trie.contains("processor"))   # False
