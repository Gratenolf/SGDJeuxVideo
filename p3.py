from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
c = MongoClient()
db = c.ng452532
db

jv = db.JeuxVideo

pipeline = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.notes":{"$ne":"null"}}},
			{"$group":{"_id":"$nom","moy":{"$avg":"$joueurs.notes"}}},
			{"$sort":{"moy":-1}},
			{"$limit":3}
]
pprint.pprint(list(jv.aggregate(pipeline)))

pipeline2 = [{"$match":{"categorie":{"$ne":"null"}}},
			{"$unwind":"$categorie"},
			{"$group":{"_id":"$categorie","count":{"$sum":1}}}
]

pprint.pprint(list(jv.aggregate(pipeline2)))


for i in jv .find() : i
