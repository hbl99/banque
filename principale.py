
from compte import *
from fonctions import *
import re
import os

choix=input("""bonjour et bienvenu dans le programme\n 1:inscrivez,\n 2:connectez-vous  \n votre choix :""")
 
if choix == 1:
  nom=raw_input('bonjour votre nom :')
  if re.search("^[A-Za-z]*[ -]?[A-Za-z]*$",nom) is not None and len(nom)>2:
          nom=arrangerNom(nom)
          

          prenom=raw_input("votre prenom :")
          if re.search("^[A-Za-z]*[ -]?[A-Za-z]*$",prenom) is not None and len(prenom) >2 :
            prenom=arrangerNom(prenom)   
            password=raw_input('votre mot de passe :')
            menbres=Compte(nom,prenom,password)
            menbres.enregistrer()

          else:
            print("saisissez un prenom valide!!!")
  else:
      print(" saisissez un nom valide !!!")   
elif choix == 2:
   donnee=[]
   nom=raw_input("nom :")
   nom=arrangerNom(nom)
   password=raw_input('password :')
   tu=(nom,password)
   cur.execute('SELECT id,solde,nom,prenom,password FROM menbre WHERE nom= %s AND password= %s',tu)

   
   
   for id,solde,nom,prenom,password in cur:
          donnee.append(id)
          donnee.append(solde)
          donnee.append(nom)
          donnee.append(prenom)
          donnee.append(password)

          menbreConnecter=Compte(nom,prenom,password,solde)
          question=input("""1:ajouter de l'argent \n 2:transfert \n 3:consulter votre solde \n 4:modifier votre password
          	                      \n 5:Retrait \n 6:dernieres operation \n""")
          if question ==1:
            menbreConnecter.ajouter(donnee[0])
          elif question == 2:
               nom=raw_input("nom :")
               nom=arrangerNom(nom)
               prenom=raw_input("prenom :")
               prenom=arrangerNom(prenom)
               tu=(nom,prenom)
               cur.execute('SELECT id,solde,nom,prenom,password FROM menbre WHERE nom = %s AND prenom=%s ',tu)
               for id,solde,nom,prenom,password in cur:
                  menbretransferer,do=ajouter(id,solde,nom,prenom,password)
                  menbreConnecter.transfert(menbretransferer,donnee[0])
          elif question == 3:
           	   menbreConnecter.consultationDuSolde()
          elif question == 4:
               menbreConnecter.setPass() 
          elif question == 5:
               menbreConnecter.retrait(donnee[0])
          elif question == 6:
            menbreConnecter.derniereTransaction(donnee[0])
             
               
          else:
            print("erreur")

else:
  print('erreur\v!!!\a')

os.system('pause') 




