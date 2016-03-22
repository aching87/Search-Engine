# Search-Engine

README

ORIGINAL_DATASET folder
- contains the original 14 document files, query file, and relevance file downloaded from the Glasgow Repository at http://ir.dcs.gla.ac.uk/resources/test_collections/lisa/ 

nltk-3.2
- this is the nltk package. To use it, it should be placed in python folder (e.g. place in C:\Program Files (x86)\Python34\Lib\site-packages folder) 

preprocessing.ipynb 
- The 14 files downloaded from the Glasgow Respository contain 6004 documents total, so the 14 files were processed and separated into the 6004 .txt documents
- Each document also has a title and a body. Create a dictionary with the doc num as the key, and the title and document as separate values -> docdict.p
-  There is one file containing a list of 35 queries, and another containing the relevant docs for each query. Create dictionaries for them -> queries.p and relevance.p 

documents folder
- contains the 6004 .txt documents
- also contains stopwords.txt 

tokenization.py
- includes functions for removing punctuation, removing stop words, and word stemming

InvertedIndex.ipynb
- includes function for directory crawler
- Create postings dictionary for the 6004 documents-> postings.p
- Create dictionary containing all words' IDF values -> invertedindex_dict.p
- Create dictionary of document lengths -> doclengths.p

search.py
- This is the main part of the search engine system.
- When run, provides a user interface that asks the user for a query, and returns the top 100 most relevant documents (including document title, document number corresponding to the .txt file, and cosine similarity to the query).  


Evaluation.ipynb
- uses the queries.p and relevance.p files to evaluate the search engine system
- evaluation metrics include precision, recall, and F-measure 

Report.pdf
- includes screen shots of test runs
- include evaluation results 
