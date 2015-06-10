import pymongo
import pprint

from pymongo import MongoClient
from flask import request

client = MongoClient()
db = client.Broadway
collection = db.musicals

def query(request):
	category = request.form["category"]
	term = request.form["search"]

	result = collection.find({category: term})
	return result
