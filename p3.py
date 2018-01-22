from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne


c=MongoClient()
db=c.ah154489
db
jv=db.JeuxVideo
import pprint

BulkTest = jv.bulk_write([
			DeleteMany({"prix":50}),
			InsertOne({"nom":"TestAjoutJeux","description":"TestDescription","prix":50,"categorie":["Action","Multijoueurs"],"auteur":"EA"})
])



pipelineb = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.note":{"$ne":"null"}}},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}}
]

pprint.pprint(list(jv.aggregate(pipelineb)))





pipeline = [{"$match":{"joueurs.pseudo":{"$ne":"null"}}},
			{"$unwind":"$joueurs"},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}},
			{"$sort":{"total":-1}},
			{"$limit":3}
]

pprint.pprint(list(jv.aggregate(pipeline)))




cursor = jv.aggregate([{"$match":{"categorie":{"$ne":"null"}}},{"$unwind":"$categorie"},{"$group":{"_id":"$categorie","count":{"$sum":1}}}])
print(list(cursor))

cursorb = jv.distinct("auteur")
print(cursorb)



for doc in jv .find({"auteur":"EA"}):doc
