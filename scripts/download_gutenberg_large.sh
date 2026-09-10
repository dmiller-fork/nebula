#!/bin/bash

mkdir -p data/gutenberg

for id in $(seq 1 1000); do
    output="data/gutenberg/$id.txt"

    echo "Downloading book $id..."

    if curl -Lf -s \
        -H "Accept-Encoding: identity" \
        "https://www.gutenberg.org/cache/epub/$id/pg$id.txt" \
        -o "$output"; then

        if file "$output" | grep -q -E 'ASCII|UTF-8|Unicode text'; then
            echo "  OK"
        else
            echo "  Not text -- removing"
            rm "$output"
        fi

    else
        echo "  Download failed"
        rm -f "$output"
    fi
done
