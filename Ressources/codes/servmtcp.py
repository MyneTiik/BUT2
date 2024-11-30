import socket
import os
from _thread import *
import json

ServerSocket = None
host = '127.0.0.1'
port = 9090
clients = []
nbclients = 0
numclient = None

# Dictionnaires pour stocker les données
global promotions
global etudiants

## Stockage des données

promotions = {}
etudiants = []

## Fonctions utilisables

def AddProm(nomprom):
    if nomprom not in promotions:
        promotions[nomprom] = []
        return "Promotion ajoutée"
    else:
        return "Promotion déjà existante"
    
     
def ShowProm():
    return promotions

def ShowEtud():
    return etudiants


def AddEtud(nom, prenom):
    for etud in etudiants:
        if etud[0] == nom and etud[1] == prenom:
            return "Étudiant déjà existant"
    etudiants.append([nom, prenom, []])
    return "Étudiant ajouté"
    
def ShowDetEtud(nom, prenom):
    for etud in etudiants:
        if etud[0] == nom and etud[1] == prenom:
            for prom, etuds in promotions.items():
                if etud in etuds:
                    return {"nom": nom, "prenom": prenom, "notes": etud[2], "promotion": prom}
            return {"nom": nom, "prenom": prenom, "notes": etud[2], "promotion": None}
    return "Étudiant non trouvé"

def ShowDetProm(nomprom):
    if nomprom in promotions:
        return promotions[nomprom]
    return "Promotion non trouvée"
        
        
def AddEtudToProm(nom, prenom, nomprom):
    if nomprom not in promotions:
        return "La promotion n'existe pas"
    for etud in etudiants:
        if nom == etud[0] and prenom == etud[1]:
            if etud not in promotions[nomprom]:
                promotions[nomprom].append(etud)
                return f"Étudiant ajouté à la promotion: {promotions}"
    return "L'étudiant n'existe pas"

def AddNote(nom, prenom, note, coefficient):
    for etud in etudiants:
        if nom == etud[0] and prenom == etud[1]:
            etud[2].append((float(note), float(coefficient)))
            return "Note ajoutée"
    return "Étudiant non trouvé"

def ShowAvg(nom, prenom):
    sum_notes = 0
    coef_tot = 0
    for elt in etudiants:
        if elt[0] == nom and elt[1] == prenom:
            for note in elt[2]:
                sum_notes += note[0]*note[1]
                coef_tot += note[1]
    return sum_notes/coef_tot
            

def ShowPromAvg(nomprom):
    nb_etud = len(promotions[nomprom])
    moy = 0
    for etud in promotions[nomprom]:
        moy += ShowAvg(etud[0], etud[1])
    return moy/nb_etud


## Fonction principale créant un thread pour chaque client 

def threaded_client(connection):
    global nbclients
    print("connection", connection)

## Boucle de réception des données du client

    while True:
        try:
            data = connection.recv(2048)
            data_decode = json.loads(data)
            print(data_decode)
            
            if data_decode["fonction"] == "AddProm":
                rep = AddProm(data_decode["nomprom"])
                connection.send(str.encode(f'{rep}\n'))
                
            elif data_decode["fonction"] == "AddEtud":
                rep = AddEtud(data_decode["nom"], data_decode["prenom"])
                connection.send(str.encode(f"{rep} \n"))
                
            elif data_decode["fonction"] == "AddEtudToProm":
                
                code = AddEtudToProm(data_decode["nom"], data_decode["prenom"], data_decode["nomprom"])
                connection.send(str.encode(f'{code} \n'))
                
            elif data_decode["fonction"] == "AddNote":
                rep = AddNote(data_decode["nom"], data_decode["prenom"], data_decode["note"], data_decode["coef"])
                connection.send(str.encode(f'{rep} \n'))
                
            elif data_decode["fonction"] == "ShowDetEtud":
                detail = ShowDetEtud(data_decode["nom"], data_decode["prenom"])
                connection.send(str.encode(f'Réussite -> {detail} \n'))
                
            elif data_decode["fonction"] == "ShowDetProm":
                detail = ShowDetProm(data_decode["nomprom"])
                connection.send(str.encode(f'Réussite -> Promotion : {data_decode["nomprom"]} - {detail} \n'))
                
            elif data_decode["fonction"] == "ShowAvg":
                moy = ShowAvg(data_decode["nom"], data_decode["prenom"])
                connection.send(str.encode(f'Réussite -> moyenne: {moy} \n'))
                
            elif data_decode["fonction"] == "ShowPromAvg":
                moy_prom = ShowPromAvg(data_decode["nomprom"])
                connection.send(str.encode(f'Réussite -> moyenne promotion: {moy_prom} \n'))
                
            elif data_decode["fonction"] == "ShowProm":
                prom = ShowProm()
                connection.send(str.encode(f'Réussite -> promotions: {prom} \n'))
                
            elif data_decode["fonction"] == "ShowEtud":
                etudi = ShowEtud()
                connection.send(str.encode(f'Réussite -> etudiants: {etudi} \n'))
                    
            elif data_decode["fonction"] == "quit":
                numclient = int(connection.recv(2048))
                break
            
            else:
                connection.send(str.encode('Invalid command\n'))
                break
        
        except json.JSONDecodeError:
            connection.send(str.encode('Invalid JSON format\n'))
        except KeyError:
            connection.send(str.encode('Commande inexistante\n'))
        except Exception as e:
            connection.send(str.encode(f'Error: {str(e)}\n'))
        
    connection.close()
        
## Fonction pour attendre les connexions des clients

def main():
    global nbclients
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    finally:
        print('Waiting for a Connection..')
        ServerSocket.listen(5)
    while True:
        client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        client.send(str.encode(str(nbclients)))
        clients.append(client)
        print("Liste clients : ", clients)
        start_new_thread(threaded_client, (client,))
        nbclients += 1
        print('Thread Number: ' + str(nbclients))

if __name__ == "__main__":
    main()