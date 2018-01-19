//1 Retourne l'ensemble des jeux d'action ou d'aventure
db.JeuxVideo.find({$or:[{"categorie":"action"},{"categorie":"aventure"}]});

//2 retourne l'ensemble des jeux d'action ayant un prix inférieur ou égale à 30
db.JeuxVideo.find({$and[{"categorie":"action"},{"prix":{$lte:30}]}});

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


//12 Afficher le top 3 des jeux possedant les meilleurs moyennes
var map = function(){
	var noteMoy = {note:this.Joueurs.note,count: 1};
	emit(this.nom,noteMoy);
};

var reduce = function(jeu,noteMoy){
	reduceNoteMoy = {note : 0, count : 0};
	for(var i=0;i<noteMoy.length;i++){
		reduceNoteMoy.note += noteMoy[i].note;
		reduceNoteMoy.count += val[i].count;
	}
	reduceNoteMoy.avg = reduceNoteMoy.note / reduceNoteMoy.count;
	return reduceNoteMoy;
};

db.JeuxVideo.mapReduce(map, reduce, {out:{inline:1}});



db.JeuxVideo.aggregate({$unwind:"$Joueurs"},{$match:{"Joueurs.notes":{$ne:null}}},{$group:{_id:"$nom",moy:{$avg:"$Joueurs.notes"}}});    ,{$sort:{moy:-1}},{$limit:3});

//13 Afficher les jeux d'action possedant un avis de "SuperFrost" ou "c3l1n3" et une note supérieur à 8


//14 Compter le nombre de jeux par auteurs


//15 Compter le nombre d'avis par joueur et leurs note maximal attribuée


//16 Compter le nombre de jeux par catégorie
