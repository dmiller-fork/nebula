# Getting started
	- clone the repo
	- go into the scripts folder and grant execution permission to download
	- download the files using make
	- then run the program, using the following commands
```
cd scripts
chmod +x download_gutenberg_large.sh
cd ..
make large
python3 nebula
```
	- note `make large` command is 1000 docs
	- it will take 5 to 30 minutes to download docs
	- about 3-8 minutes to build inverted index
	- and .5-2 seconds to run queries
	- if this is to slow, use `make data` instead for only 30 docs
```
cd scripts
chmod +x download_gutenberg_data.sh
cd ..
make data
python3 nebula
```
	- you can always start over with `make clean`
	- type `exit` or `quit` to exit program

# developers only

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

## Running tests
	- jump into the tests folder to run tests individually
	- alternatively, use make:
```
make run_all
```
