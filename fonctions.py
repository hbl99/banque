from compte import *
def arrangerNom(nom):
	nom=nom.upper().capitalize()
	return nom
def ajouter(id,solde,nom,prenom,password):
    donnee=[]
    donnee.append(id)
    donnee.append(solde)
    donnee.append(nom)
    donnee.append(prenom)
    donnee.append(password)
    return Compte(nom,prenom,password,solde),donnee
