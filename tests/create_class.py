import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from libnebula import InvertedIndex

if __name__ == "__main__":
	index = InvertedIndex()
	assert  index.index == {}
	print("class test passed")
