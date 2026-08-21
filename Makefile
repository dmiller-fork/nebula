.PHONY: test data clean

test:
	./scripts/download_gutenberg_test.sh

data:
	./scripts/download_gutenberg_data.sh

clean:
	rm -f data/gutenberg/*.txt
