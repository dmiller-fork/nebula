# Getting started
## setting up your environment
	- create this file .git/hooks/pre-commit
```
#!/bin/sh

maxsize=$((10 * 1024 * 1024))  # 10 MB
total=0

for file in $(git diff --cached --name-only); do
    [ -f "$file" ] || continue

    size=$(wc -c < "$file")
    total=$((total + size))
done

if [ "$total" -gt "$maxsize" ]; then
    echo "Error: staged files total more than 10 MB"
    echo "Total: $total bytes"
    exit 1
fi

exit 0
```
Then turn it on:
```
chmod +x .git/hooks/pre-commit
```
	- finally, make sure your .gitignore is not tracking the data folder
```
data/
```


## Downloading the data
	- first try a test download

```
chmod +x scripts/download_gutenberg_test.sh
make test
```
	- when ready perform full download

```
chmod +x scripts/download_gutenberg_data.sh
make data
```
	- you can check the size of your data folder with the following command:
```
du -sh data
```
