import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne
import sys
import io
import pprint
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

c=MongoClient()
#modifier l'utilisateur de la BD
db=c.ng452532

jv=db.JeuxVideo

# requete 1 
print("\nSuppression de tous les jeux ayant un prix fixe a 50 et ajout d'un jeu test : \n")
BulkTest = jv.bulk_write([
			DeleteMany({"prix":50}),
			InsertOne({"nom":"TestAjoutJeux","description":"TestDescription","prix":50,"categorie":["Action","Multijoueurs"],"auteur":"EA"})
])
jv.find_one({"prix":50})


# requete 2 
print("\nAffichage du top 3 des jeux possedant les meilleurs moyennes : \n")
pipeline = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.notes":{"$ne":"null"}}},
			{"$group":{"_id":"$nom","moy":{"$avg":"$joueurs.notes"}}},
			{"$sort":{"moy":-1}},
			{"$limit":3}
]
pprint.pprint(list(jv.aggregate(pipeline)))


# requete 3
print("\nAffichage du nombre de jeux disponible par categorie : \n")
pipeline2 = [{"$match":{"categorie":{"$ne":"null"}}},
			{"$unwind":"$categorie"},
			{"$group":{"_id":"$categorie","count":{"$sum":1}}}
]
pprint.pprint(list(jv.aggregate(pipeline2)))


# requete 4
print("\nAffichage de l'ensemble de la collection : \n")
for i in jv.find() :
	pprint.pprint(i)
	print("\n")


# requete 5
print("\nAffichage du nombre d'avis par joueur et leurs note maximal attribuee : \n")
pipeline3 = [{"$unwind":"$joueurs"},
			{"$match":{"joueurs.note":{"$ne":"null"}}},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}}
]
pprint.pprint(list(jv.aggregate(pipeline3)))


# requete 6
print("\nAffichage du top 3 des meilleurs commentateurs : \n")
pipeline4 = [{"$match":{"joueurs.pseudo":{"$ne":"null"}}},
			{"$unwind":"$joueurs"},
			{"$group":{"_id":"$joueurs.pseudo","total":{"$sum":1}}},
			{"$sort":{"total":-1}},
			{"$limit":3}
]
pprint.pprint(list(jv.aggregate(pipeline4)))


# requete 7
print("\nAffichage de l'ensemble des auteurs : \n")
cursorb = jv.distinct("auteur")
print(cursorb)



# Partie création de fonction


# méthode 1
def recherche(editeur):
	print("\nListe des jeux de l'editeur ",editeur," : ")
	for i in jv.find({"auteur":editeur}):
		print(" -",i["nom"])
		print("\tPrix : ",i["prix"],"euro")
		print("\tCategorie : ")
		for j in i["categorie"]:
			print("\t - ",j)

#ensemble de tests pour la méthode
recherche("Nintendo")
recherche("Michel vedette")
recherche("Valve")


# méthode 2
def recherche(editeur, categorie):
	print("\nListe des jeux de l'editeur ",editeur," sur la categorie ",categorie," : ")
	for i in jv.find({"auteur":editeur,"categorie":categorie}):
		print(" -",i["nom"])
		print("\tPrix : ",i["prix"],"euro")

#ensemble de tests pour la méthode
recherche("EA","Action")
recherche("Lee sensei 3","Action")


# méthode 3
def rechercheJeu(jeu):
	print("\n",jeu," : ")
	for i in jv.find({"nom":jeu}):
		print("\tDescription : ",i["description"])
		print("\tPrix : ",i["prix"],"euro")
		print("\tCategorie : ")
		for j in i["categorie"]:
			print("\t - ",j)
		print("\n\tavis : ")
		for j in i["joueurs"]:
			print("\t\t",j["pseudo"])
			print("\t\tNote : ",j["notes"])
			print("\t\tCommentaire : ",j["avis"],"\n")

#ensemble de tests pour la méthode
rechercheJeu("Mountain")
rechercheJeu("Portal 2")




