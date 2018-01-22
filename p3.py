import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

c=MongoClient()
db=c.ah154489
db
jv=db.JeuxVideo
import pprint

print("\nSuppression de tous les jeux ayant un prix fixe a 50 et ajout d'un jeu test : \n")
BulkTest = jv.bulk_write([
			DeleteMany({"prix":50}),
			InsertOne({"nom":"TestAjoutJeux","description":"TestDescription","prix":50,"categorie":["Action","Multijoueurs"],"auteur":"EA"})
])

jv.find_one({"prix":50})

print("\nAffichage du top 3 des jeux possedant les meilleurs moyennes : \n")
pipeline = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.notes":{"$ne":"null"}}},
			{"$group":{"_id":"$nom","moy":{"$avg":"$joueurs.notes"}}},
			{"$sort":{"moy":-1}},
			{"$limit":3}
]
pprint.pprint(list(jv.aggregate(pipeline)))

print("\nAffichage du nombre de jeux disponible par categorie : \n")
pipeline2 = [{"$match":{"categorie":{"$ne":"null"}}},
			{"$unwind":"$categorie"},
			{"$group":{"_id":"$categorie","count":{"$sum":1}}}
]
pprint.pprint(list(jv.aggregate(pipeline2)))

print("\nAffichage de l'ensemble de la collection : \n")
for i in jv .find() : i

print("\nAffichage du nombre d'avis par joueur et leurs note maximal attribuee : \n")
pipeline3 = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.note":{"$ne":"null"}}},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}}
]
pprint.pprint(list(jv.aggregate(pipeline3)))

print("\nAffichage du top 3 des meilleurs commentateurs : \n")
pipeline4 = [{"$match":{"joueurs.pseudo":{"$ne":"null"}}},
			{"$unwind":"$joueurs"},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}},
			{"$sort":{"total":-1}},
			{"$limit":3}
]
pprint.pprint(list(jv.aggregate(pipeline4)))

print("\nAffichage de l'ensemble des auteurs : \n")
cursorb = jv.distinct("auteur")
print(cursorb)

print("\nAffichage des jeux de l'auteur EA : \n")

chaine =[]
for doc in jv.find({"auteur":"EA"}):
	print(doc)
	
