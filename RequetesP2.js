//1 Retourne l'ensemble des jeux d'action ou d'aventure
db.JeuxVideo.find({$or:[{"categorie":"Action"},{"categorie":"Aventure"}]});


//2 retourne l'ensemble des jeux d'action ayant un prix inférieur ou égale à 30
db.JeuxVideo.find({$and:[{"categorie":"Action"},{"prix":{$lte:30}}]});


//3 retourne le nombre total de jeux ayant un prix supérieur ou égal à 30
db.JeuxVideo.find({"prix":{$gte:30}}).count();


//4 suppression du pseudo "DarkSasuke91"
db.Projet.remove({"Joueurs.pseudo":"DarkSasuke91"});

//5 Afficher la liste complete des catégories existantes
db.JeuxVideo.distinct("categorie");


//6 Afficher les 3 premiers jeux d'un auteur
db.Projet.find({"auteur":"EA"}).limit(3);

//7 Afficher l'ensemble des auteurs existants
db.JeuxVideo.distinct("auteur");


//8 Afficher les noms des jeux possedant plus de 3 avis
db.Projet.find({Joueurs:{$exists:true},$where:'this.Joueurs.length > 3'});

//9 Afficher le top 3 des joueurs donnant un avis
db.JeuxVideo.aggregate({$match:{"Joueurs.pseudo":{$ne:null}}},{$unwind:"$Joueurs"},{$group:{_id:"$Joueurs.pseudo",total:{$sum:1}}},{$sort:{total:-1}},{$limit:3});


//10 Lister les jeux suivant leurs moyennes par ordre décroissant
db.JeuxVideo.aggregate({$unwind:"$Joueurs"},{$match:{"Joueurs.notes":{$ne:null}}},{$group:{_id:"$nom",moy:{$avg:"$Joueurs.notes"}}},{$sort:{moy:-1}});


//11 Afficher le top 3 des jeux possedant les meilleurs moyennes
db.JeuxVideo.aggregate({$unwind:"$Joueurs"},{$match:{"Joueurs.notes":{$ne:null}}},{$group:{_id:"$nom",moy:{$avg:"$Joueurs.notes"}}},{$sort:{moy:-1}},{$limit:3});


//12 Afficher les jeux d'action possedant un avis de "SuperFrost" ou "c3l1n3" et une note supérieur à 8
db.Projet.aggregate({$match:{$and:[{$or:[{"Joueurs.pseudo":"SuperFrost","Joueurs.pseudo":"c3l1n3"}]},{"Joueurs.note":{$gte:8}}]}});

//13 Compter le nombre de jeux par auteurs
var map = function(){
	var nbJeu = {count : 1};
	emit(this.auteur,nbJeu);
};
var reduce = function(auteur,jeux){
	reduceNbJeux = {count : 0};
	for(var i=0;i<jeux.length;i++){
		reduceNbJeux.count += jeux[i].count;
	}
	return reduceNbJeux;
};
db.JeuxVideo.mapReduce(map, reduce, {out:{inline:1}});


//14 Compter le nombre d'avis par joueur et leurs note maximal attribuée
db.Projet.aggregate({$unwind:"$Joueurs"},{$match:{"Joueurs.note":{$ne:null}}},{$group:{_id:"$Joueurs.pseudo",total:{$sum:1}}});

//15 Compter le nombre de jeux par catégorie
db.JeuxVideo.aggregate({$match:{"categorie":{$ne:null}}},{$unwind:"$categorie"},{$group:{_id:"$categorie",count:{$sum:1}}});


//16 ajouter à chaque jeu d'Action un Joueur nommé testAvis donnant une note de 8 et un avis "testAvis"
db.JeuxVideo.updateMany({"categorie":"Action"},{$push:{"Joueurs":{"pseudo":"testAvis","avis":"testAvis","notes":8}}},{multi:true});


//17 renommer l'auteur IA en EA
db.JeuxVideo.replaceOne({"auteur":"IA"},{"auteur":"EA"});



