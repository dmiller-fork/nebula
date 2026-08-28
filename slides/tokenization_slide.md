	- After creating the inverted index and the search results functions, we tested the search results against a very small data set.
	- see the test at tests/medium_query.py
	- We tested for the words "treasure" and "Jim", and only recieved 1 result
```
Running tests/medium_query.py
index size: 24036
defaultdict(<function SearchResults.__init__.<locals>.<lambda> at 0x1011aeae0>, {'84': defaultdict(<class 'int'>, {'treasure': 1})})
```
	- next we ran the same test with grep
```
 grep -n "treasure" 84.txt
935:treasures known to few besides myself. I have described myself as always
3845:a treasure which would fully reward his toil and hazard.
4010:possession of these treasures gave me extreme delight; I now continually
4154:never driven away. I asked, it is true, for greater treasures than a
6176:Elizabeth I possessed a treasure, alas, balanced by those horrors of
```
	- Grep gave better results. We needed to add a better tokenizer.
	- Words are randomly capitlized and punctuation is an issue
	- After a little research, we found:
```
import string

word = word.strip(string.punctuation).lower()

```
	- note rstrip() means right strip, so only right punctuation is removed
	- strip() does both, so getting rid of quotations
	- Fixing this one bug, caused the results to change:
```
Running tests/medium_query.py
index size: 15733
defaultdict(<function SearchResults.__init__.<locals>.<lambda> at 0x102901fe0>, {'1342': defaultdict(<class 'int'>, {'treasure': 1}), '84': defaultdict(<class 'int'>, {'treasure': 2})})
```
	- The results now align more closely with the expected results, as tested against grep. Adding stemming or plural checking would be a design decision.

## unicode
	- We created a sort list of words by frequency, and printed those out.
	- There were still a lot of words with double quotes at the end.
	- The double quotes were unicode, so string.punctuation was not catching it.
	- the following code cleans that up:
```
	PUNCTUATION = string.punctuation + "“”‘’"
	word = word.strip(PUNCTUATION).lower()
```
	- python isn't a compiled langauge, the interpreter will run those two lines for every iteration. To fix this, the PUNCTUATION regex needs to be defined at the top of the method rather than in the for loop.

