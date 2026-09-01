## Introduction TF-IDF
```
TF = word count of each “query_term” in each "book_instance" FROM INDEX / 
		total word count in "book_instance" FROM BOOKS 

IDF = log(
		total documents FROM BOOKS/ 
			documents containing "query_term" FROM INDEX
		)
```
	- TF is local component, how good is this query against this document
	- IDF is a global component, how discriminating is the query against the entire corpus
## Literature Review
	- [1] Spärck Jones (1972), "A statistical interpretation of term specificity and its application in retrieval" — the original statistical justification for IDF. This gives you the historical/theoretical basis for inverse document frequency.
	- Salton, Allan & Buckley (1994), “Automatic Structuring and Retrieval of Large Text Files” — gives you Salton's vector-space/term-weighting framework and retrieval methodology.
Lee, Chuang & Seamons (1997), “Document Ranking and the Vector-Space Model” — particularly useful for your implementation because it compares the different weighting and normalization choices rather than treating TF-IDF as one immutable formula.

## An examle with three books and three query terms

Treasure Island:
  treasure:
    TF: count("treasure" in TI) FROM INDEX
        / total words in TI FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "treasure" FROM INDEX)

  bones:
    TF: count("bones" in TI) FROM INDEX
        / total words in TI FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "bones" FROM INDEX)

  adultery:
    TF: count("adultery" in TI) FROM INDEX
        / total words in TI FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "adultery" FROM INDEX)


The Scarlet Letter:
  treasure:
    TF: count("treasure" in SL) FROM INDEX
        / total words in SL FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "treasure" FROM INDEX)

  bones:
    TF: count("bones" in SL) FROM INDEX
        / total words in SL FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "bones" FROM INDEX)

  adultery:
    TF: count("adultery" in SL) FROM INDEX
        / total words in SL FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "adultery" FROM INDEX)


Frankenstein:
  treasure:
    TF: count("treasure" in F) FROM INDEX
        / total words in F FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "treasure" FROM INDEX)

  bones:
    TF: count("bones" in F) FROM INDEX
        / total words in F FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "bones" FROM INDEX)

  adultery:
    TF: count("adultery" in F) FROM INDEX
        / total words in F FROM BOOKS
    IDF: log(total docs FROM BOOKS
             / docs containing "adultery" FROM INDEX)

Then score each book:
Treasure Island =
    TF-IDF(treasure)
  + TF-IDF(bones)
  + TF-IDF(adultery)

Scarlet Letter =
    TF-IDF(treasure)
  + TF-IDF(bones)
  + TF-IDF(adultery)

Frankenstein =
    TF-IDF(treasure)
  + TF-IDF(bones)
  + TF-IDF(adultery)


## designing the algorithm
	- for TF, total words in each book is constant, so pre-calculate
	- for IDF, total number of documents is constant, so pre-calculate
	- for TF, total count of each query_term needs to be calculated on the fly
	- for IDF, number of docs containing query term needs to be calculated on the fly

### intermediate steps
	- create a search results index (forward index) from the inverted index based on query terms
	- then perform a for loop on the search results to get the needed parameters on the fly to calculate the TF-IDF score
	- the search results are used in two ways:
		1) the first is to perform TF-IDF
		2) the second is to generate snippet presentations

### optimizations
	- construct a TF-IDF utility object to precalulate constants from books
	- if TF = 0, no need to calculate IDF
