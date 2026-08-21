#!/bin/bash

mkdir -p data/gutenberg

for id in 1342 11 84; do
    curl -L \
        "https://www.gutenberg.org/cache/epub/$id/pg$id.txt" \
        -o "data/gutenberg/$id.txt"
done
