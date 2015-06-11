import math
import tfidf
import nltk
from nltk.corpus import wordnet as wn

#TO DO: 1. Find appropriate constants c1 and c2. 
#       2. Give relevancy score to topic sentences and concluding sentences
#           a higher value than non-topic sentences.
#           --> This can be done by looking at additional line of white space.
#       3. Add in other useful pieces of information that can be used to calculate in-depth articles.
#       4. Fix current errors in formatting for relevancy score to read wordnet.
#       5. Possible to include formal vs informal(?)





my_tfidf = tfidf.TfIdf()
document1 = "sample.txt" #insert new text document and put in file location.

my_tfidf.add_input_document(document1)

#tfidf implemented in tfidf.py

def in_depth_rating(document1, searchWord):

    #document1 should be location of file.
    #each
    desiredDoc = document1
    docSet = set()
    keywords = [] #keywords for the document
    with open(desiredDoc) as f:
        lineText = f.readlines()
    for i in range(len(lineText)):
        my_tfidf.add_input_document(lineText[i]) #inserts document into tfidf
    for i in range(len(lineText)):
        keywords.append(my_tfidf.get_doc_keywords(lineText[i]))
    for i in range(len(lineText)): #creates a set of the words. 
        words = lineText[i].strip()
        for j in words:
            docSet.add(j)

    def numOfArticles():
        return my_tfidf.get_num_docs()

    def content_length(desiredDoc):
        docLen = 0
        for i in range(len(lineText)):
            words =lineText[i].strip(" ")
            docLen += len(words)
        return docLen

    def relevancy_score(desiredDoc):
        #Each word has score between 0 to 1 in terms of similarity. "None" is returned
        #there is no similarity. 

##      searchWordwn = wn.synset("'" + searchWord + ".n.01'")
        relevancyScore = 0
        
##        for i in range(len(keywords)):
##            for j in range(len(keywords[i])):
##                currentWord = keywords[i][j]
##                currentWordwn = wn.synset("'" + currentWord + ".n.01'")
##                currentWordScore = wn.path_similarity(searchWordwn,currentWordwn)
##
##                if currentWordScore != None:
##                    relevancyScore += currentWordScore
##
        return relevancyScore
                

    def textRichness(desiredDoc):
        #calculates ratio for number of different words used as a measure.
        #The set does not add repeated words.
        return len(docSet)/content_length(desiredDoc)


    contentScore = textRichness(desiredDoc) * content_length(desiredDoc)
    relevancyScore = relevancy_score(desiredDoc)
    c1 = 10 #relevancy score constant.
    c2 = 3 #contentScore constant.
    inDepthRating = c1*relevancyScore + c2*contentScore

    
    return inDepthRating
    
print(in_depth_rating(document1, "sample"))
