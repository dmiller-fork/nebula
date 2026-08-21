Upload a one-page project proposal that includes:

# Project title
	- Nebula Search
# Group members
	- Daniel Miller
	- Mert Tuncer
# Project plan, including:
## a brief description of the project,
	- a search engine with separate filter words and snippet words
## the main tasks,
	- corpus intake -> tokenize words in corpus-> build inverted index & trie
	- tokenize query -> inverted index lookup -> calculate TF-IDF -> k-rank heap & full sort 
	- extract keyword window -> rank windows -> return top snippet each doc
	- create benchmarks (define query and relevant snippets, % relevant/precision)
	- experiments:
		- test different tokenizations (domain specific tokenizations)
		- test different TF or IDF formulas (see wikipedia tf-idf) 
		- test custom query patterns (filter words, snippet words, high value words)
	- Plot BigO, empirical runtime, and benchmarks
	- UI
## the roles and responsibilities assigned to each team member.
	- Daniel is in charge of inverted index creation
	- Mert is in chart of retrieval
	- Daniel is in charge of snippet creation
	- Mert is in charge of benchmarks
# from the slides:
## Project requirements
	- core structure/algorithm
	- unit tests (empty,single-element,cyclic/duplicate,disconnected cases)
	- Big-O analysis
	- empirical runtime study (at least one plot of time vs. input size)
	- user interface (Jupyter notebook, CLI, or Web interface)


## Course anchors: 
	- hash maps, tries, heaps, sets, strings. 
## Stretch concept
	- inverted index with trie prefix search and heap-based top-k ranking (TF-IDF).
## Problem
	- build an inverted index
	- Use inverted index to return the top-ranked pages for a query
	- returns prefix autocomplete and snippets.

## have one slide on exploring data set (cleaning, outliers)
## decide on whether you want test and validation data
## everyone must present something (both mert and daniel, on tuesday)
 - from week 7
