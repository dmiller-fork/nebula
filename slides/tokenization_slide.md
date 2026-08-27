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
	- After a little research, we found:
```
import string

word = word.rstrip(string.punctuation)

```
	- note rstrip() means right strip, so only right punctuation is removed
	- Fixing this one bug, caused the results to change:
```
Running tests/medium_query.py
index size: 15733
defaultdict(<function SearchResults.__init__.<locals>.<lambda> at 0x102901fe0>, {'1342': defaultdict(<class 'int'>, {'treasure': 1}), '84': defaultdict(<class 'int'>, {'treasure': 2})})
```
	- The results now align more closely with the expected results, as tested against grep. Adding stemming or plural checking would be a design decision.
