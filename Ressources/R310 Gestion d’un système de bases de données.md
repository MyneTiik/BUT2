
[Installer MongoDB sur linux](https://linux.how2shout.com/how-to-install-mongodb-6-0-server-on-ubuntu-22-04/) 

`$ sudo systemctl start (/status) mongod`

Connexion à MongoSH : 

`$ mongosh -u "root" -p "azerty" --authenticationDatabase "admin"`

### **Vérifier le statut de MongoDB :**

``$ sudo systemctl status mongod``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdaPmMeqkZBCHWv7NeoXs2ei_PBqQIY1HNLnYoR821MYDvKVAV1uxpC8qujOYRXXjFKh_aPtWIsYw1fslrk3DO8G1vaJmYt5KcKrkwuD317WumHC_tcX1UD2ZhiqXJ3RmFCw_YR5RJl9bYt6XhlcdY4Ljk?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Créer la base :**

``test> use tp``
#### **Importer le json :**

``$ mongoimport --host "localhost:27017" --username "root" --password "azerty" --authenticationDatabase "admin" --collection "movies" --db "tp1" --file movies.json``

(il a fallu enlever le --jsonArray car le format ne correspondait pas)

``tp1> show collections``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdA0v4l9N-o4X3mku9i-3fTo-0oforqGdBag7w4ytKLaaMm0o8EgHPf0Qy8vkScF4rE_o3_wGOcqufUAl5bVLMgToyix64ZFHQIyR7JY2_vm8IAh_xhbnFJipBCqnvljnUmaBdiqFBvbp_nrt2XPnph-A1U?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Vérifier l’importation :**

``tp1> db.movies.find()``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdMicuA77dlOF-s1kfnl7BZF_IUajquivP5EKodU2NdARcivRfdWDmCGkJazV1RF9xw2Z0a8027hPj989mZNoC_DlcStFYPU1FykM9TWXUag--ddTrwGem9EubSpkj5BC8y_HAMeSgekEMRfyrdfGNYuyk?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Compter le nombre de docs :**

``tp1> db.runCommand({count:’movies’})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdob3RP2sUGk66MIzxFLG54AqFbilLgNqgX5J7K7lAfcz5FXUm9Tq2bK_WHuEO1hB08EkgrxFnGztdpWdD_xu3oAG3EUbYKKWANJyddQ-ehqaOUwcRNA5m-Zy_FXDS4K5g5OY5CzXRQcfNmU4pAVSEaLKWn?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Les films qui commencent par “Star” :**

``tp1> db.movies.find({ "title": { $regex: /^Star/ }})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdGu3NgeAoTqn49hJnb1L1oAOh71YiDlprOz9yEIurDZcfN4wZ_AubuPmvR3w9qYudvCekRyFCaVhJOhADeYKL4W1kuF3MXl5kqFt6zvQbqXfw-WvpN3NUQsUHSPibXho25DdrmSMIodTqOF3M3nvIXDY56?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Avoir le nombre de films qui commencent par “Star” :**

``tp1> db.movies.countDocuments({ "title": { $regex: /^Star/ }})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfFxZHYA-jy6tuTbKJiWqG3GP5m7IortyhIXaEmsf34m8GPzpuWPU_dXmWHshSdeNs_H1f1GOnUzBI91NW_pci8bTGAXXRjbJ1VHGMu3dkvMCBOgYvI6AoYoFTU3E2ouW2cMWV0n21Lk_7s23gNe83Caaaz?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Nombre de films de comédie :**

``tp1> db.movies.countDocuments({ "genres": { $regex: /Comedy/ }})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHISIIwLE_EwjeSlLMT0fcBLqKu6wAhL6DIeEA4j19KHvE13zsYrpG_tPwlCH5WxLVWFXei4Bxsi2Q7jMSBnwQ-Cc62JDjAqtn7VMqymreF41vR7CaiVOWnzZhfEFGKp4gnc1IJJKxS64JP0IJC-hQ_ZM?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Liste des comédies :**

``tp1> db.movies.find({ "genres": { $regex: /Comedy/ }})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcR7dPRYpMI7SeU3kVSctPyEzvSvv_jCC5skZDbamCxFGZIrCMW3AnJ20VpDekXcv05_6gYtyAB4KAJFaq9ZzVJF4xkND9m_esPjVDgwyey3u-6tWndpO8Kux1yVd5N9_ABO2tIgBMg8uNIJXLVcbqp1pEh?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Pareil mais avec les films d’action :**

``tp1> db.movies.countDocuments({ "genres": { $regex: /Action/ }})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdfocKkXSfX91Yus9Fmi0T-OcIczcoT5krr7BubGhDoeUDhPJsAG_aUFtSh8i1UWRWvTFGQwGBSQQnIGQ55PRpk-Mpu6HPztzY1iNAEqJSbJ1jFFuMcztNsFl8_cTvpsjekCuPAjtjrooXg-1KbJ4DZ5_Iy?key=iAVe7TE_kzSEuRWw_w-lIw)

``tp1> db.movies.find({ "genres": { $regex: /Action/ }})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdIc5qxFwLGcuq82QiM2ikV8CPzi3jvvtsOtO-TXLr3k6wL6CkGKpkjzE5Y4udl_AG-GoY753aa8OVBfdoyE4FIw-bEK1bjCdl4kd9JS6zKPqkElC6UV_kmxgRygk8dkQy14yc5GhFI8HyORFg5_0hdtuM9?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Afficher la liste des films qui sont sortis en 1977 et qui contiennent « IV » dans le « title » :**

``tp1> db.movies.find({ $and: [{ "title": { $regex: /1977/ }}, { "title": { $regex: /IV/i } } ] })``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeL60DoQVV8VzFZoi6aKLBXM-kKGGuQKnt_P-pxobB8vX0x_bYY23F8Mn8pIuPSAw1CQ6q0TQVW2WihpBNmpB4hZQ2qe0yw1M86Uz73yi4_3f3wQI8mAqL8Z8NK2tCb53L-ldWNT-pjqcfGjXq07h537YDG?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Récupérer l’année de sortie du film et d’en faire une champ “release_date” :**

``tp1> db.movies.find().forEach(function(x) {db.movies.updateOne({ "_id":x._id},{ $set: { "release_date": x.title.substring(x.title.length-5,x.title.length-1)}});});``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfJG295Sne4pgyD4LRmjjZDKxHae9J-0hE4TQirBlpMJ8BO7MBilbmM7YvNBRVZxB0BV-yJSrz9cZTuorImZK9sgktK5jT7MbKvK3_jJUOdJiNjg4lrSQ8_U_vu-tQQ0OTeMzkW7mgZIdCNFaK7jXNPx150?key=iAVe7TE_kzSEuRWw_w-lIw)

**

Cette ligne de code JavaScript utilise MongoDB pour faire des opérations sur une collection de documents. Voici une explication simple de chaque partie :

1. db.movies.find() :
	- Cela récupère tous les documents de la collection nommée movies.


2. .forEach(function(x){ ... }); :
    - Chaque document récupéré par le find() est passé un par un dans cette fonction. Chaque document est appelé x dans la fonction.

3. db.movies.updateOne({"_id":x._id}, {...}); :

    - Pour chaque document, une mise à jour est effectuée sur ce document en particulier.
    - Le document est identifié par son champ unique _id (ici x._id).


4. {$set: {"release_date": ...}} :
    
	- L'opération de mise à jour utilise $set pour ajouter ou mettre à jour un champ spécifique dans le document. Ici, le champ release_date est mis à jour.

5. x.title.substring(x.title.length-5,x.title.length-1) :
    
	- Cela extrait une partie de la chaîne de caractères title (titre du document).

Plus précisément, ça prend les 4 caractères avant la fin du titre (length - 5 à length - 1). Cela pourrait représenter, par exemple, une année (si les titres se terminent par une année).
### **En résumé :

*Pour chaque document dans la collection movies, cette ligne de code met à jour le champ release_date en prenant les 4 derniers caractères du champ title (potentiellement l'année) et les stocke dans release_date.*

# **TD 2:

### **Question 1:**

``db.td2.find( {}, { _id: 0, cuisine: 1})``

*(td2 = restaurants)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfOQsnzpnlLexXuepFv3baeSdVZDGxqpNiR0D_lKnoGkmFmv45b_sZd-BOxy53QZO4xZX56lfZCIrQpQFwwQJGWy5FrA4fT8uEF5Gwa2phLrG-SWOEV8SEbWWXWukw4b1DPEun_sWYyY1UqlAf0voZAehoA?key=iAVe7TE_kzSEuRWw_w-lIw)

### **Question 2:**

``db.td2.distinct("grades.grade")``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXebKHqd4xNZXfHrWJAw5cu3g1SXPWv8j4SfnNJS8jpbCV1N0jzPBR8_5pTIv-nbpVOJsvgI2-lrYrPQU0_1-hJYRRuCz9Q35omEGpcmLKHwwH_hL4pBzwplJsl-ncn9K2etTkztD9BKgO1OugmA4HHAaL6h?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question 3:**

``db.td2.count({cuisine : "French"})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd2B-B8ZCg5vgS1wK9pelBpqerAuHSfTcGdblJkHzjzRgO8ROOKcKS4K2E4sjTwA1y08LrRoCarzjNEd-YciC2oyNJ5brnVclqGbhRmgvUz1jARRJVSHzHGRqbpIoCKfmHa2peQQO1A2ZFZeDmkDUdxaB3X?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question 4:**

``db.td2.count({"address.street": "Central Avenue"})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeR7goYKwztXtfEuTFedl9AD2ElT5CoCkzQClZjo3JmNZbq0tEsCAXsce14HQJemy7X3ye7sAR1VyZNreAQ5u-BkgiqXS_uBaNiEgGsCTMLPua719xtu1LR7t8VvopgdHTDlD1WIBTkJFiiFP1EPIXFe8E?key=iAVe7TE_kzSEuRWw_w-lIw) 
### **Question 5:**

``db.td2.count({"grades.score": {$gt : 50}})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfNytdfV6sVKUlXnouuJxrxwnyIW2Ob8AA3LODuBn9PbcgntXmELF6hpRqix9-9OdrbkdsQpMVIMVzPa83uJq5qi9NOHQvJO8EEOFrPZq2KbxVE1dNm67FSmdzB0pWx_JtQmQt721TVPQ7QskX3ngecsKPV?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question 6:**

``db.td2.find( {}, { _id: 0, name: 1, "address.building": 1, "address.street": 1})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUC1bF6SVVN0XQbMpJoS-Z9FudEIpjKLt2xgOHRpFmReMoGlg-tVJBf1dJsx-Bv9GyutNem9StpwA51v9crLO5nLrSyyVRdEJ8Gn7XEbhMWIzEaRGhNmIuNZi9lvk1pyewQ6WRUMnN52urJLTmg85kImoM?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question 7:**

``db.td2.find( {}, { _id: 0, name: "Burger King", "address.borough": 1})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfrQpovwpa8-K-BEImdh4GMOyW30zpJIydW5UJqBVZwL3rV_Fw7bVi1nq3879fgo_ys4RrmYNgdRVYT_2hGw-FCUWoV-soSCKeZsR81OX5dgBGYDB5pjhdHyVpctPWEAJGlud7FNocOo58JHRWRVHjyK3vj?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question 8:**

``db.td2.find({"address.street": { $in: ["Union Street", "Union Square"]}},{_id:0 , name: 1, "address.street": 1})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcw1rCA-21GglLAu38AGBcORVZYrwSH2pRzoKRDgJWlLlsO6DToUWfbM0OEFlfuenQKtDmwFokf3DLrTDF-ygJt3okP2tkcZrQIvJ-TSztExQVqx8BR2-Hu7f6tliSiKkT_sAzVfcYgsJoAxyfdbTYkWGNv?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question 9:**

``db.td2.find({"address.coord.1": {$gt : 40.90}},{_id: 0, name: 1, "address.coord": 1})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSP9E2ZrzWH5fvGaRKo6rO9vfRyp5AKuWANYXzmeQO4vK5yQsKuciSE6WrX3Wyle9BcCOIriNrlhygbV3iQ51qsUvJyJVVUTxCfDW-Cc46W1lSf9iQ40dCpXSu1H3YgPEjyXdWDT9UUym2zDQyY43iCrXM?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question 10:**

``db.td2.find({},{_id: 0, name: 1, "grades.grade": 1, "grades.score": 1, "grades.grade" : "A", "grades.score":"0"})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc_160CdWG806dRI4FEgCRtTwh6gz0km9Nw2dIAlhU62lJ4pR05nwCrUP80hGej2urYwzk3zg0dKOQQe3wY_4dzXWUmZFYy4-3IvdVYLzYaHHDwgZV26uWy8UDOL_K6tKND0dWyeQO_1D-rZYjkWOO8MFpW?key=iAVe7TE_kzSEuRWw_w-lIw)
### **Question Bonus 1:**

``db.td2.find({"address.street": {$regex: /Union/}},{_id: 0, name: 1, "address.street": 1,})``

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc6gv-hKKIyQ0F9GaPBeWym1DSslnXjOh6VAKZo8S7vXZQ_j6OXs61vb-IQZdJz0Khb-Og7U8eRR18eVbWAFM62E0A4PC3MD_rPu9j_HWLrupsEyIXMMj9CCc1uZQAd7-neTflXj6lKSdmdNXDFZYZYhIy3?key=iAVe7TE_kzSEuRWw_w-lIw)