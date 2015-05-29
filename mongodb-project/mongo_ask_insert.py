import pymongo
import pprint

from pymongo import MongoClient
from flask import request

client = MongoClient()
db = client.Broadway
collection = db.musicals

def get_user_input(request):
	show = {}
	mainNum = 1
	mainNum = str(mainNum)

	title = request.form["title"]
	show["title"] = title

	writers = request.form["writers"]
	if writers.find(",") == True:
		show["playwrights"] = writers.split(", ")
	else:
		show["playwright"] = writers

	opening_year = request.form["opening_year"]
	if opening_year.find(",") == True:
		show["openings"] = int([opening_year.split(", ")])
	else:
		show["opening"] = opening_year

	instruments = request.form["instruments"]
	if instruments.find(",") == True:
		show["instruments"] = instruments.split(", ")
	else:
		show["instrument"] = instruments

	songs = request.form["songs"]
	show["songs"] = [songs.split(",")]

	while request.form.has_key("main_character" + mainNum):
		main_character = request.form["main_character" + mainNum]
		character = {}
		character["name"] = main_character

		vox = request.form["vox" + mainNum]
		character["vocal_part"] = vox

		belt = request.form["belt" + mainNum]
		character["belt"] = belt

		vrange = request.form["vrange" + mainNum]
		character["vocal_range"] = vrange

		age = int(request.form["age" + mainNum])
		character["age"] = age

		gender = request.form["gender" + mainNum]
		character["gender"] = gender
		show["main_characters"].append(character)

		mainNum = mainNum + 1

	collection.insert(show)
	return show
