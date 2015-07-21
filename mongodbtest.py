import datetime
import re
from alchemyapi import AlchemyAPI
from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

##client = MongoClient ('localhost', 27017)
##db = client.test_database
##
##post = {"author": "Mike",
##        "text": "My first blog post!",
##        "tags": ["mongodb", "python", "pymongo"],
##        "date": datetime.datetime.utcnow()}
##posts = db.posts
##posts = db.posts
##post_id = posts.insert_one(post).inserted_id
##
##for record in posts.find():
##    print(record["author"])

app = Flask(__name__)
api = Api(app)
alchemyapi = AlchemyAPI()

class dbtest(Resource):
    def midpoint(arr):
        a = len(arr)
        mid = a/2
        return arr[mid]





api.add_resource(dbtest, '/')
if __name__ == '__main__':
    app.run(debug=True)
