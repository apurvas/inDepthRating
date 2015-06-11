import math
import tfidf
import nltk
from nltk.corpus import wordnet as wn
import time
my_tfidf = tfidf.TfIdf()
document1 = "cosmopolitan.txt" #insert new text document and put in file location.
document2 = "nytimes.txt"
document3 = "cnn.txt"
document4 = "bob.txt"
my_tfidf.add_input_document(document1)

#tfidf implemented in tfidf.py
start_time = time.time()
def in_depth_rating(document1, searchWord):
##  start_time = time.time()
    #document1 should be location of file.
    #each
    desiredDoc = document1
    docSet = set()
    keywords = []
    with open(document1) as f:
        data = f.read()
    keywords = my_tfidf.get_doc_keywords(data)
    with open(desiredDoc) as f:
        lineText = f.readlines()
    for i in range(len(lineText)): #creates a set of the words. 
        words = lineText[i].strip()
        for j in words:
            docSet.add(j)


    def content_length(desiredDoc):
        docLen = 0

    

    def relevancy_score(desiredDoc):
        #Each word has score between 0 to 1 in terms of similarity. "None" is returned
        #there is no similarity. 
        newWord =searchWord + ".n.01" 
        searchWordwn = wn.synset(newWord)
##        print (newWord)
##        print (searchWordwn)
        relevancyScore = 0
        currentWordScore = 0
        memo = {}
        for i in range(len(keywords)):
                currentWord = keywords[i][0]
                if currentWord in memo:
                    currentWordScore = memo[currentWord]
                    if currentWordScore != None:
                        relevancyScore += currentWordScore
                else:
                    if wn.synsets(currentWord, pos = wn.NOUN) != []:
                        currentWordwn = wn.synsets(currentWord, pos = wn.NOUN)[0]
                        currentWordScore = wn.path_similarity(searchWordwn,currentWordwn)
                        memo[currentWord] = currentWordScore

                    if currentWordScore != None:
                        relevancyScore += currentWordScore

        return relevancyScore
                

    def textRichness(desiredDoc):
        #calculates ratio for number of different words used as a measure.
        return len(docSet)

    contentScore = len(docSet)
    c1 = 10 #relevancy score constant.
    c2 = 3 #contentScore constant.
    relevancyScore = relevancy_score(desiredDoc)
    inDepthRating = c1*relevancyScore + c2*contentScore
    return (relevancyScore, contentScore, inDepthRating)

##print("--- %s seconds ---" % (time.time() - start_time))    
    

##print(in_depth_rating(document2,"transexual"))
##print ("___________________________________________________________")
##print(in_depth_rating(document1,"transexual"))
##print (wn.synsets("just"))
##print (wn.path_similarity(wn.synset('just.a.01'),wn.synset('merely.r.01')))
print (in_depth_rating(document3, "gender"))
##print ("___________________________________________________________")

                          

print(in_depth_rating(document2,"transexual"))
##print("'" + 'kitchen' + ".n.01'")
##newWord = "kitchen"
##print (wn.synsets(newWord))
##print (wn.synset('kitchen.n.01'))
##newWord2 = "'" + 'kitchen' + '.n.01'
##print ("""'A word that needs quotation marks' """)
##print ("""' """ + newWord + """n.01'""")
##a = newWord + """.n.01"""
##print (wn.synset(a))
##print ((wn.synsets("your")))
print (in_depth_rating(document1, "kitchen"))
##print (wn.path_similarity(wn.synsets("was", pos = wn.NOUN)[0],wn.synset("kitchen.n.01")))
##print (wn.synset("kitchen.n.01"))
print("--- %s seconds ---" % (time.time() - start_time)) 
