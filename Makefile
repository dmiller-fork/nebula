.PHONY: data clean

data:
	./scripts/download_gutenberg.sh

clean:
	rm -f data/gutenberg/*.txt
