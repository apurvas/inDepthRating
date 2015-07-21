import math
import tfidf
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
import time
import re
from alchemyapi import AlchemyAPI
from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database


app = Flask(__name__)
api = Api(app)


alchemyapi = AlchemyAPI()

my_tfidf = tfidf.TfIdf()
document1 = "cosmopolitan.txt" #insert new text document and put in file location.
document2 = "nytimes.txt"
document3 = "cnn.txt"
document4 = "bob.txt"
my_tfidf.add_input_document(document1)
databaseRecord = {}
class ShardingRouter(object):

    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return 'default'

    def allow_syncdb(self, db, model):
        return 'default'
#tfidf implemented in tfidf.py
start_time = time.time()

class flaskAPI(Resource):
    def get(self):
        a = inDepthRating()
        c = a.in_depth_rating(document2,"transexual")
        post1 = {"relevancyscore": c[0], 'content score': c[1], 'Final Depth Rating': c[2]}
        posts1 = db.posts1
        post1_id = posts1.insert_one(post1).inserted_id
        fin = []
        final = " "
        for record in posts1.find():
             fin.append(str(record["relevancyscore"]))
             fin.append("   ")
            
        return ",".join(fin)
            
        

class inDepthRating():
    def in_depth_rating(self, document1, searchWord):
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
        def imp_sent_splitter(desiredDoc):
          with open(desiredDoc) as t:
              data1 = t.read()
          a = data1.split("\n")
          sent_list = []
          top_sent_list = []
          conc_sent_list = []
          for i in a:
                if i != ['']:
                  sent_tokenizer = sent_tokenize(i)
                  sent_list.extend(sent_tokenizer)
                  if sent_tokenizer != []:
                       top_sent_list.append(sent_tokenizer[0])
                       conc_sent_list.append(sent_tokenizer[len(sent_tokenizer)-1])
          ##print(len(top_sent_list))
          ##print(len(conc_sent_list))
          ##print (data1)

          sum1 = 0
          ##print(len(sent_list))
          ##print(conc_sent_list)
            
        
          ##re.split('\s{4,}',text) --> Splitting with indents
          ##data1.split("\n\n") --> splitting with new lines.

        def sent_score(desiredDoc):
            myText = data
            response = alchemyapi.sentiment("text", myText)
            return response

        

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
        response = sent_score(desiredDoc)
        ##print ("Sentiment: ", response["docSentiment"]["type"])
        databaseRecord = {'relevancy score': relevancyScore, 'content score': contentScore, 'Final Depth Rating': inDepthRating}
        ##db.insert(databaseRecord);
        return (relevancyScore, contentScore, inDepthRating)

        def get(self,document1,searchWord):
            return print("Hello")
        


##results = db.find() ##finds all the documents
##    for record in db.test.find()[0]:
##        print( record['relevancy score'] + ' ,' +  record['content score'] + ' ,' + record['Final Depth Rating'])
##a = inDepthRating()
##c = a.in_depth_rating(document2, "transexual")
##print(c[0])
##post1 = {"relevancyscore": c[0], 'content score': c[1], 'Final Depth Rating': c[2]}
##posts1 = db.posts1
##post1_id = posts1.insert_one(post1).inserted_id
##print (post1_id)
##for record in posts1.find():
##    print (record["relevancyscore"])
api.add_resource(flaskAPI, '/')


if __name__ == '__main__':
    app.run(debug=True)
        



    

print("--- %s seconds ---" % (time.time() - start_time)) 
