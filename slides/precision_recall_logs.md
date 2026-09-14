$: python3 recall_and_precision_adventure.py
starting test...
query is 5 terms: treasure voyage adventure pirates swords
number of docs in dataset: 964
number of relevant docs in dataset: 130
number of docs returned: 20
number of relevant docs in results: 12
Precision@20: 60.00%
Recall@20:    9.23%
Max possible recall given docs returned: 15.38%

$: python3 recall_and_precision_adventure_tf_only.py 
starting test...
query is 5 terms: treasure voyage adventure irates swords
number of docs in dataset: 964
number of relevant docs in dataset: 130
number of docs returned: 20
number of relevant docs in results: 13
Precision@20: 65.00%
Recall@20:    10.00%
Max possible recall given docs returned: 15.38%

$: python3 recall_and_precision_adventure_idf_only.py 
starting test...
query is 5 terms: treasure voyage adventure pirates swords
number of docs in dataset: 964
number of relevant docs in dataset: 130
number of docs returned: 20
number of relevant docs in results: 3
Precision@20: 15.00%
Recall@20:    2.31%
Max possible recall given docs returned: 15.38%

$: python3 recall_and_precision_scifi.py    
starting test...
query is 5 terms: spaceship future technology alien planet
number of docs in dataset: 964
number of relevant docs in dataset: 33
number of docs returned: 20
number of relevant docs in results: 3
Precision@20: 15.00%
Recall@20:    9.09%
Max possible recall given docs returned: 60.61%

$: python3 recall_and_precision_scifi_tf_only.py 
starting test...
query is 5 terms: spaceship future technology alien planet
number of docs in dataset: 964
number of relevant docs in dataset: 33
number of docs returned: 20
number of relevant docs in results: 4
Precision@20: 20.00%
Recall@20:    12.12%
Max possible recall given docs returned: 60.61%

python3 recall_and_precision_scifi_idf_only.py 
starting test...
query is 5 terms: spaceship future technology alien planet
number of docs in dataset: 964
number of relevant docs in dataset: 33
number of docs returned: 20
number of relevant docs in results: 0
Precision@20: 0.00%
Recall@20:    0.00%
Max possible recall given docs returned: 60.61%

$: python3 recall_and_precision_treasureisland.py
starting test...
query is 4 terms: voyage yo-ho-ho travel weapons
['103', '829', '598', '605', '487', '15', '793', '265', '521', '534', '861', '597', '578', '684', '548', '561', '806', '800', '120', '899']
number of docs in dataset: 964
number of relevant docs in dataset: 1
number of docs returned: 20
number of relevant docs in results: 1
Precision@20: 5.00%
Recall@20:    100.00%
Max possible recall given docs returned: 100%

python3 recall_and_precision_treasureisland_tf_only.py 
starting test...
query is 4 terms: voyage yo-ho-ho travel weapons
['851', '103', '15', '597', '534', '793', '984', '598', '578', '605', '561', '800', '265', '806', '861', '521', '684', '487', '548', '899']
number of docs in dataset: 964
number of relevant docs in dataset: 1
number of docs returned: 20
number of relevant docs in results: 0
Precision@20: 0.00%
Recall@20:    0.00%
Max possible recall given docs returned: 100%

python3 recall_and_precision_treasureisland_idf_only.py 
starting test...
query is 4 terms: voyage yo-ho-ho travel weapons
['15', '289', '329', '472', '505', '466', '699', '673', '665', '670', '896', '120', '499', '883', '895', '706', '894', '713', '666', '622']
number of docs in dataset: 964
number of relevant docs in dataset: 1
number of docs returned: 20
number of relevant docs in results: 1
Precision@20: 5.00%
Recall@20:    100.00%
Max possible recall given docs returned: 100%
