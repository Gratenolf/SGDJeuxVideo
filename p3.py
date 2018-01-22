from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime


c=MongoClient()
db=c.ah154489
db
jv=db.JeuxVideo

pipelineb = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.note":{"$ne":"null"}}},
			{"$group":{"_id":"$joueurs.pseudo",
			"total":{"$sum":1}}}
]
import pprint
pprint.pprint(list(jv.aggregate(pipelineb)))


pipeline = [{"$match":{"joueurs.pseudo":{"$ne":"null"}}},
			{"$unwind":"$joueurs"},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}},
			{"$sort":{"total":-1}},
			{"$limit":3}
]
import pprint
pprint.pprint(list(jv.aggregate(pipeline)))




cursor = db.JeuxVideo.aggregate([{"$match":{"categorie":{"$ne":"null"}}},{"$unwind":"$categorie"},{"$group":{"_id":"$categorie","count":{"$sum":1}}}])
print(list(cursor))

cursorb = db.JeuxVideo.distinct("auteur")
print(cursorb)



for doc in db.JeuxVideo .find("auteur":"EA"):doc
