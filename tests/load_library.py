import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from hello import hello

if __name__ == "__main__":
    assert hello() == "Hello, world!"
    print("hello test passed")
