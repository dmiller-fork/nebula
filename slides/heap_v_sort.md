# the method
	- in benchmarks ran the heap and sort algorithms using the time module

## the results
	- the main data set is 30 documents
	- this returned the following results:
```
query is two terms: treasure the
Heap: 0.000014 seconds
Sort: 0.000008 seconds
```
	- the heap algorithm is longer so we tried with 100 docs instead
	- this caused some problems because the downloaded docs weren't all text
	- but after removing the bad files:
```
query is two terms: treasure the
Heap: 0.000020 seconds
Sort: 0.000010 seconds
```
	- still no good, needed to try 1000:
```
Heap: 0.000085 seconds
Sort: 0.000124 seconds
```
	- that answer shows the relationship we expected
	- heap is faster than sort
