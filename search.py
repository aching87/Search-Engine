from tkinter import *
from tokenization import *
import pickle
import math

postings = pickle.load( open( "postings.p", "rb" ) ) # load postings dictionary
invertedindex_dict= pickle.load( open( "invertedindex_dict.p", "rb" ) ) # load IDF values dictionary
doclengths= pickle.load( open( "doclengths.p", "rb" ) ) # load dictionary with document lengths
docdict=pickle.load(open("docdict.p","rb"))# load dictionary containing docnum, doc title, and doc content

def process_query():
    #tokenize query 
    query=ment.get()# get search term(s) that user entered in GUI
    query2=query.lower()#change all letters to lowercse
    query3= removePunctuation(query2)# remove punctuation
    query4=removestopwords(query3) #remove stop words
    query5=stemwords(query4) #stem words, returns a list of words

    # term frequencies in query
    querydict={}
    for w in query5:
        if querydict.get(w,0)==0:
            querydict[w]=1 # if token is not already in querydict, add to querydict and assign count to 1
        else:
            querydict[w]+=1 # if token is already in querydict, add 1 to token's count 

    # get query length
    querylength=0
    queryuniquewords=list(set(query5)) # set of unique words in query 
    for word in queryuniquewords:
        if invertedindex_dict.get(word)==None: # if query word is not in inverted index, ignore 
            pass
        else:
            idf=invertedindex_dict.get(word)# if query word is in inverted index, get IDF 
            count=querydict[word] 
            querylength+=(idf*count)**2
            querylength=querylength**0.5 # calculate query length 

    ## INVERTED INDEX RETRIEVAL
    R={} # empty hashmap to store retrieved documents with scores 
    for t in querydict: # for each token in query
        if invertedindex_dict.get(t)==None: # if query word is not in inverted index, ignore
            pass
        else:
            idf=invertedindex_dict[t] # term's IDF
            termcount=querydict[t] # count of term in query 
            weight= termcount*idf
    
            d = postings[t] # get query terms from inverted index 
            if d!=0:
                length=len(d) # num of docs with term 
                for doc in d:# for each doc with term 
                    doc=doc
                    C=d[doc] # term frequency in D 
                    if R.get(doc,0)==0:
                        R[doc]=0
                    R[doc]+=idf*C
    normalizedDscore={}
    for D in R: # for each retrieved document in R 
        S = R[D] # current accumulated score of D
        Y = doclengths[D] # length of D
        normalizedDscore[D]=S/(querylength*Y) # normalize the query-doc similarity, final is cosine similarity
    # shorten doc name so it only contains doc num
    for x in normalizedDscore.keys():
        newdoc = x.replace('C:\\Users\\Amy\\Google Drive\\CSC575\\lisa\\documents\\', '')
        newdoc2=newdoc.replace('.txt', '')
        normalizedDscore[newdoc2] = normalizedDscore.pop(x)
        
   
    # Sort the results based on document score            
    sortedscores = sorted(normalizedDscore.items(), key=lambda x:x[1],reverse = True)
    if(len(sortedscores)==0):
        sorry="Sorry, no matches were found" # if there were no retrieved documents
        mlabel2=Label(mGui,text=sorry).pack()
    elif len(sortedscores)<=100: # if there are <=100 retrieved documents
        mlabel2=Text(mGui, width=90)
        for i in range(len(sortedscores)):
            x=sortedscores[i][0]# get doc num
            doctitle=docdict[int(x)][0]# get doc title for doc num
            docinfo= doctitle + str(sortedscores[i])
            mlabel2.insert(END, docinfo + '\n\n')
        mlabel2.pack()
    else: # there are >100 retrieved documents
        topsortedscores=sortedscores[:100] # get top 100 most similar docs, and show these to the user
        mlabel2=Text(mGui, width=90)
        for i in range(len(topsortedscores)):
            x=topsortedscores[i][0]# get doc num
            doctitle=docdict[int(x)][0]# get doc title for doc num
            docinfo= doctitle + str(topsortedscores[i])
            mlabel2.insert(END, docinfo + '\n\n')
        mlabel2.pack()

# Create GUI
mGui = Tk() 
ment=StringVar()
mGui.title('LISA Search') 

mLabel=Label(mGui, text="Library and Information Science Abstracts (LISA) is an international abstracting and indexing tool designed for library professionals and other information specialists.\n Please enter your search query and click on the 'Submit Query' button. \n A list of the top 100 documents (including document title, document number, and the document's 0-1 similarity to your query) that may be relevant to your search will be printed below.\n If there are less than 101 documents relevant to your query, then all relevant documents will be printed below.").pack()
mbutton=Button(mGui, text='Submit Query', command=process_query, bg='dark gray').pack()

mEntry=Entry(mGui,width=100, bd=3, textvariable=ment).pack()
