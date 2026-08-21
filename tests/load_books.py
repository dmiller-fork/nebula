from pathlib import Path
print("Hello from load_books.py")

books = {}

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "gutenberg"

for file in DATA_DIR.glob("*.txt"):
	books[file.stem] = file.read_text()
	print(file.stem)
	print(file.name)
