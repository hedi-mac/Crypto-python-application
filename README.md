# Crypto-python-application

**1 Réalisation :**

L’objectif principale de ce projet et de récolter des avis sur les
cryptomonnaies, les analysés avec une méthode de classification pour
traitement de langage naturel (NLP) puis de fournir les résultats à
l’utilisateur de notre programme.

La collecte des avis pour notre cas et réparti sur deux partis :

  - Collecte des avis sur les cryptomonnaies depuis Twitter :

> Pour cela nous avons besoins d’utiliser ‘Twitter API’ et spécification
> la bibliothèque **‘Tweepy’** pour le langage python. En effet,
> ‘Twitter API’ nous permet des requêtes sont composées d'opérateurs
> qui sont utilisés pour faire correspondre une variété d'attributs de
> Tweet. Twitter API offre plusieurs rôles pour son utilisation. Pour le
> droit d’accès ‘Essentiel’ ou ‘Elevé’, la requête peut comporter
> **512** caractères et **1024** pour les accès ‘à la recherche
> universitaire’. Nous avons le droit à effectuer 450 requêtes toutes
> les 15 minutes sont permises.

  - Collecte des articles sur les cryptomonnaies depuis les sites web :

> Pour effectuer cette tache nous avons besoin de récupérer une liste
> des liens des sites web contenant des articles sur les cryptomonnaies
> à analyser et dans une période spécifique en utilisant ‘GOOGLE API’
> permettant 40 requêtes par heure. Puis l’extraction du contenue des
> articles, pour cela nous avons besoin d’utiliser la bibliothèque
> **‘BeautifulSoup’** pour effectuer le ‘Web Scraping’.

Une fois les avis sont collectés, nous devons les analysées. Nous
analysons les tweets qui représente un texte cours contenant des avis
des utilisateurs de Twitter qui l’on poster. Concrètement parlant,
répondre à ce besoin implique l’utilisation d’une bibliothèque NLP
basée sur le ‘Machine Learning’ permettant d’analyser le texte et de
sortir avec une décision si ce texte représente un avis positif ou
négatif sur l’état de la cryptomonnaie. Pour l’analyse des articles qui
représente un texte écrit par des experts dans le domaine des finances
et des cryptomonnaies, nous sommes face à une contrainte supplémentaire
qui est la langueur du texte. La solution pour cela c’est de mettre en
place une phase de résumer des textes avant la phase de leurs analyses.
Ce qu’on entend par l’idée de résumer des articles c’est l’utilisation
d’une bibliothèque NLP spécifique au domaine des cryptomonnaies pour
conserver le vrai sens de l’article.

Enfin, après avoir les avis analysés nous devons représenter le résultat
pour l’utilisateur de cet incrément. En effet, le client désir
visualiser les résultats à la suite de l’exécution du code python. Pour
répondre à ce besoin, nous présenterons les résultats des analyses sous
forme d’un fichier CSV en plus des statistiques qu’offre la bibliothèque
Python ‘Matplotlib’.

A la fin de ce sprint le livrable doit comporter les composantes
énoncées tout d’abord et ceci comme le montre la *Figure1* si dessous.

![image](https://user-images.githubusercontent.com/32374946/192635923-db9f7cc2-1dfc-43e9-b2fb-fb56936262ef.png)
> *Figure 1 Schéma architecture du projet*

**2 Réalisation :**

![image](https://user-images.githubusercontent.com/32374946/192635996-f8608830-1b03-4f22-a0e3-40ff9131e086.png)
> *Figure 2 Execution test methodes d'analyse*
> 
![image](https://user-images.githubusercontent.com/32374946/192636062-80e75e25-9954-443b-bb69-cd8b0fc414e7.png)
>
> *Figure 3 Test temps execution methodes d'analyse*
> 
![image](https://user-images.githubusercontent.com/32374946/192636080-75e24910-abeb-477d-86a2-8edb1e8914b5.png)
>
> *Figure 4 Fichier CSV resultat*
> 
![image](https://user-images.githubusercontent.com/32374946/192636111-3a42eaf5-443a-4ca0-9169-65ff9140b17a.png)
>
> *Figure 5 Statistiques resultat*







