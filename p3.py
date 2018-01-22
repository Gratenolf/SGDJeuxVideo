from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
c = MongoClient()
db = c.ng452532

jv = db.JeuxVideo

print("\nAffichage du top 3 des jeux possedant les meilleurs moyennes : \n")
pipeline = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.notes":{"$ne":"null"}}},
			{"$group":{"_id":"$nom","moy":{"$avg":"$joueurs.notes"}}},
			{"$sort":{"moy":-1}},
			{"$limit":3}
]
pprint.pprint(list(jv.aggregate(pipeline)))

print("\nAffichage du nombre de jeux disponible par catégorie : \n")
pipeline2 = [{"$match":{"categorie":{"$ne":"null"}}},
			{"$unwind":"$categorie"},
			{"$group":{"_id":"$categorie","count":{"$sum":1}}}
]
pprint.pprint(list(jv.aggregate(pipeline2)))

print("\nAffichage de l'ensemble de la collection : \n")
for i in jv .find() : i

print("\nAffichage du nombre d'avis par joueur et leurs note maximal attribuée : \n")
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
for doc in jv .find({"auteur":"EA"}):doc
