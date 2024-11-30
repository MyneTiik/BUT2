import socket 
import os 
from _thread import *
import json 
import time

ClientSocket = None 
host = '127.0.0.1' 
port = 9090 
myNumber = 0 

## connexion au serveur

def main():
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    ClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    
    try:        
        ClientSocket.connect((host, port))    
    except socket.error as e:        
        print(str(e))    
    finally:        
        print("connected to Server !")        
        myNumber = int(ClientSocket.recv(1024))        
        print("myNumber client received : ", myNumber)    
    start_new_thread(threaded_server, (ClientSocket, myNumber))  
      
## Fonction pour envoyer les commandes au serveur
      
    while True:
        msg = {}     
        
        time.sleep(1)
        print("\nAjouter une promotion : AddProm")
        print("Ajouter étudiant : AddEtud")
        print("---------------------------------")
        print("Ajouter une Note : AddNote")
        print("Ajouter étudiant à une promotion : AddEtudToProm")
        print("Afficher la moyenne : ShowAvg")
        print("Afficher la moyenne d'une promotion : ShowPromAvg")
        print("---------------------------------")
        print("Afficher Promotion : ShowProm")
        print("Afficher Etudiant : ShowEtud")
        print("Afficher le détail d'un étudiant : ShowDetEtud")
        print("Afficher les détails d'une promotion : ShowDetProm")

        print("Quitter : quit \n")
        fonction = input("Que voulez-vous faire ?  ")
        
        
        if fonction == "AddProm":
            nomprom = input("Nom de la promotion : ")
            msg["fonction"] = fonction
            msg["nomprom"] = nomprom
        
        elif fonction == "AddEtud":
            nom = input("Nom : ")
            prenom = input("Prenom : ")
            msg["fonction"] = fonction
            msg["nom"] = nom
            msg["prenom"] = prenom
            
        elif fonction == "AddEtudToProm":
            nom = input("Nom : ")
            prenom = input("Prenom : ")
            nomprom = input("Nom de la promotion : ")
            msg["fonction"] = fonction
            msg["nom"] = nom
            msg["prenom"] = prenom
            msg["nomprom"] = nomprom
            
        elif fonction == "AddNote":
            nom = input("Nom : ")
            prenom = input("Prenom : ")
            note = input("Note : ")
            coef = input("Coefficient : ")
            msg["fonction"] = fonction
            msg["nom"] = nom
            msg["prenom"] = prenom
            msg["note"] = note
            msg["coef"] = coef
            
        elif fonction == "ShowDetEtud":
            nom = input("Nom : ")
            prenom = input("Prenom : ")
            msg["fonction"] = fonction
            msg["nom"] = nom
            msg["prenom"] = prenom
            
        elif fonction == "ShowDetProm":
            nom = input("Nom de la promotion : ")
            msg["fonction"] = fonction
            msg["nomprom"] = nom
            
        elif fonction == "ShowAvg":
            nom = input("Nom : ")
            prenom = input("Prenom : ")
            msg["fonction"] = fonction
            msg["nom"] = nom
            msg["prenom"] = prenom
            
        elif fonction == "ShowPromAvg":
            nom = input("Nom de la promotion : ")
            msg["fonction"] = fonction
            msg["nomprom"] = nom
        
        elif fonction == "ShowProm":
            msg["fonction"] = fonction
            
        elif fonction == "ShowEtud":
            msg["fonction"] = fonction
    
        elif fonction == "quit":
            break
        

        message = json.dumps(msg)
    
        ClientSocket.send(str.encode(message))        

## 

def threaded_server(connection, num):    
    while True:
        response = connection.recv(1024)
        if not response : 
            print("Connection closed by server.")
            break
        print(response.decode('utf-8'))


       
if __name__== "__main__":  main()