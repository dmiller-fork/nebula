while read -r id; do
    curl -L \
        "https://www.gutenberg.org/cache/epub/$id/pg$id.txt" \
        -o "data/gutenberg/$id.txt"
done < scripts/gutenberg_ids.txt
