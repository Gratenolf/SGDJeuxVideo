//1 Retourne l'ensemble des jeux d'action ou d'aventure
db.JeuxVideo.find({$or:[{"categorie":"Action"},{"categorie":"Aventure"}]});


//2 retourne l'ensemble des jeux d'action ayant un prix inférieur ou égale à 30
db.JeuxVideo.find({$and:[{"categorie":"Action"},{"prix":{$lte:30}}]});


//3 retourne le nombre total de jeux ayant un prix supérieur ou égal à 30
db.JeuxVideo.find({"prix":{$gte:30}}).count();


//4 met à jour le pseudo "repley" en "bishop"  


//5 suppression du pseudo "DarkSasuke91"


//6 Afficher la liste complete des catégories existantes
db.JeuxVideo.distinct("categorie");


//7 Afficher les 3 premiers jeux d'un auteur


//8 Afficher l'ensemble des auteurs existants
db.JeuxVideo.distinct("auteur");


//9 Afficher les noms des jeux possedant plus de 3 avis


//10 Afficher le top 3 des joueurs donnant un avis
db.JeuxVideo.aggregate({$match:{"Joueurs.pseudo":{$ne:null}}},{$unwind:"$Joueurs"},{$group:{_id:"$Joueurs.pseudo",total:{$sum:1}}},{$sort:{total:-1}},{$limit:3});


//11 Lister les jeux suivant leurs moyennes par ordre décroissant
db.JeuxVideo.aggregate({$unwind:"$Joueurs"},{$match:{"Joueurs.notes":{$ne:null}}},{$group:{_id:"$nom",moy:{$avg:"$Joueurs.notes"}}},{$sort:{moy:-1}});


//12 Afficher le top 3 des jeux possedant les meilleurs moyennes
db.JeuxVideo.aggregate({$unwind:"$Joueurs"},{$match:{"Joueurs.notes":{$ne:null}}},{$group:{_id:"$nom",moy:{$avg:"$Joueurs.notes"}}},{$sort:{moy:-1}},{$limit:3});


//13 Afficher les jeux d'action possedant un avis de "SuperFrost" ou "c3l1n3" et une note supérieur à 8


//14 Compter le nombre de jeux par auteurs
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


//15 Compter le nombre d'avis par joueur et leurs note maximal attribuée


//16 Compter le nombre de jeux par catégorie
db.JeuxVideo.aggregate({$match:{"categorie":{$ne:null}}},{$unwind:"$categorie"},{$group:{_id:"$categorie",count:{$sum:1}}});


//17 ajouter à chaque jeu d'Action un Joueur nommé testAvis donnant une note de 8 et un avis "testAvis"
db.JeuxVideo.updateMany({"categorie":"Action"},{$push:{"Joueurs":{"pseudo":"testAvis","avis":"testAvis","notes":8}}},{multi:true});


//18 renommer l'auteur IA en EA
db.JeuxVideo.replaceOne({"auteur":"IA"},{"auteur":"EA"});
