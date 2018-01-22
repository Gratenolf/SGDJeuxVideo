from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
c = MongoClient()
db = c.ng452532

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




pipeline3 = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.note":{"$ne":"null"}}},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}}
]
pprint.pprint(list(jv.aggregate(pipeline3)))


pipeline4 = [{"$match":{"joueurs.pseudo":{"$ne":"null"}}},
			{"$unwind":"$joueurs"},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}},
			{"$sort":{"total":-1}},
			{"$limit":3}
]
pprint.pprint(list(jv.aggregate(pipeline4)))




cursor = jv.aggregate([{"$match":{"categorie":{"$ne":"null"}}},{"$unwind":"$categorie"},{"$group":{"_id":"$categorie","count":{"$sum":1}}}])
print(list(cursor))

cursorb = jv.distinct("auteur")
print(cursorb)



for doc in jv .find({"auteur":"EA"}):doc
