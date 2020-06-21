#coding:utf8
import mysql.connector
conn=mysql.connector.connect(
  user='root',
  password='root',
  host='localhost',
  database='compte',
  )
cur=conn.cursor()



class Compte():
  def __init__(self,nom,prenom,password,solde=0):
    self.nom=nom
    self.prenom=prenom
    self.solde=solde
    self.password=password 
  

  def ajouter(self,id):
    montant=input('montant :')
    if montant > 0:
     

       montant=float(montant)
       self.solde +=montant
       tu=(self.solde,self.nom,id)
       cur.execute("UPDATE menbre SET solde=%s WHERE nom=%s AND id=%s",tu)
       conn.commit()
       conn.close()
       print("Mr {} le  montant de {} a ete ajouter avec succes".format(self.nom,montant))
       print("votre nouveau solde est de {}".format(self.solde))
      
    else:
      print("votre montant est inferieur a 0")


  def transfert(self,cible,id):

   
    montant=input('le montant sil vous plait')
    montant=float(montant)
    motDepass=raw_input("votre mot de passe  s il vous plait :")
    if motDepass==self.password:
           taxe=montant*0.03  
           self.solde-=taxe 
           if self.solde >0 and self.solde > montant and montant >0:
             
             cible.recevoir(montant)
             self.solde-= montant
             tu=(montant,taxe,self.nom,self.prenom,self.password)
             cur.execute("UPDATE menbre SET solde=solde- %s-%s WHERE nom = %s AND prenom=%s AND password=%s",tu)
             ti=(id,montant,taxe,cible.nom)
             cur.execute("""INSERT INTO transaction(id_menbre,date_transaction,montant,taxe,type_transaction,destinataire) 
              VALUES(%s,NOW(),%s,%s,'Transfert',%s)""",ti)
             
             print("vous avez effectuer un transfert de {}".format(montant))

             print("votre nouveau solde est de :{}".format(self.solde))
             conn.commit()
           else:
             print("votre solde est insuffisant pour effectuer cette operation!!!") 
             self.solde +=taxe 
    else:
      print("votre mot de passe  n est pas valide")
      
  
  def setPass(self):
    ancienMotDePas=raw_input('entrer votre ancien mot de passe:')
    if ancienMotDePas == self.password:
      nouveauMotDePass=raw_input('veuillez entrer votre nouveu mot de passe:')
      
      tu=(nouveauMotDePass,self.password,self.nom)
      cur.execute(" UPDATE menbre SET password= %s WHERE password=%s AND nom= %s",tu)
      conn.commit()

      print('votre mot de passe a ete remplacer avec succes')
    else:
       print("Mot de passe incorrect ") 
   
  def retrait(self,id):
    
    montantARetirer=input("veuiller saisir le montant a retirer")
    montantARetirer=float(montantARetirer)
    motDepass=raw_input("veuillez saisir votre mot de passe ")
    if motDepass == self.password:
           taxe=montantARetirer*0.03
           self.solde -=taxe
           if self.solde >0 and self.solde > montantARetirer and montantARetirer> 0:
             self.solde -=montantARetirer
             tu=(montantARetirer,taxe,self.nom,self.prenom)
             cur.execute('UPDATE menbre SET solde=solde-%s-%s WHERE nom=%s AND prenom =%s',tu)
             ti=(id,montantARetirer,taxe)
             cur.execute("""INSERT INTO transaction(id_menbre,date_transaction,montant,taxe,type_transaction) 
              VALUES(%s,NOW(),%s,%s,'Retrait')""",ti)
            
             print("{} vous avez retirer un montant de {} dans votre compte".format(self.nom,montantARetirer))
             print("votre nouveau solde est de:{}".format(self.solde))
             conn.commit()
             conn.close()
           else:
             print('impossible effectuer l operation') 
             self.solde +=taxe 
    
    else:
       print('mot de passe incorect ') 
       

  def enregistrer(self):
      
      tu=(self.solde,self.nom,self.prenom,self.password)
      cur.execute("""INSERT INTO menbre(solde,nom,prenom,password,date_inscrption) VALUES(%s,%s,%s,%s,NOW())""",tu)
      conn.commit()
      conn.close()
      print("{} votre compte a ete bien enregistrer".format(self.nom))
  
  def consultationDuSolde(self):
    print("vous avez {} dans votre compte".format(self.solde))

  def recevoir(self,montant):
     if montant > 0:
      tu=(montant,self.nom,self.prenom,self.password)
      cur.execute("UPDATE menbre SET solde =solde + %s WHERE nom =%s AND prenom=%s AND password=%s",tu)  
      conn.commit()
      print("{} vous avez recut un transfert de {}".format(self.nom,montant))
     else:
       print("erreur") 
  def derniereTransaction(self,id):
     tu=(id,self.nom)
     cur.execute("""SELECT transaction.date_transaction,transaction.montant,transaction.type_transaction
      FROM transaction INNER JOIN menbre ON menbre.id=transaction.id_menbre WHERE transaction.id_menbre= %s 
       AND menbre.nom=%s""",tu)
     
     for date,montant,type_transaction in cur:
        print("{},montant :{},{}".format(date,montant,type_transaction))
     conn.commit()