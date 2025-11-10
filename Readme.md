# Étude sur l’analyse d’images pour la réalisation d’inventaires de biodiversité

## Installation
Pour avoir la même version de python que moi vous pouvez utiliser anaconda pour génerer les versions des packages. 
```
conda env create -f environment.yml
```
ou ci-dessous pour modifier le nom par défaut.
```
conda env create -f environment.yml --name [nom de l'environement]
```
Et la commande pour activer l'environement: 
```
conda activate [nom de l'environement]
```

## Contexte
Dans le cadre d’un projet d’étude de la dynamique de recolonisation de parcelles laissées en friche, on souhaite étudier la faisabilité de faire un suivi de l’évolution de la faune et de la flore à l’aide de drones. Pour cela nous aurions besoin de différentes méthodes de vision par ordinateur, d’analyses d’image et de reconnaissance.

> Exemple concret :  
Un drone survole une parcelle et capture des images/vidéos. A l’aide des ces données nous pouvons extraire des informations utiles pour le suivi des caractéristiques (à définir selon l’utilité et la faisabilité) de la parcelle. Nous avons ensuite la possibilité de naviguer la zone une nouvelle fois dans le futur pour obtenir l’évolution des ces caractéristiques.

## Dataset

Actuellement nous ne possédons pas encore de données (images/vidéos) enregistrées par un drone sur une parcelle d’intérêt.

Il y a deux pistes qui sont envisagées pour l'acquisition futur de prise de vue par drone: 
Images hyperspectrales: technologie permettant d'obtenir l'image d'une scène dans un grand nombre (généralement plus d'une centaine) de bandes spectrales à la fois étroites et contiguës.
Images classiques (RGB)

Étant donné l’absence d’image et la difficulté de collecter un grand nombre d’exemples, nous devons chercher des datasets déjà existants.

> Dataset à explorer:
> - ISPRS (International Society for Remote Sensing) https://www.isprs.org/resources/datasets/Default.aspx 
> - Land Cover from Aerial Imagery (Landcorver.ia) https://landcover.ai.linuxpolska.com/ 
> - IGN (Institut géographique national) https://www.ign.fr/ 
> - sPlotOpen, https://onlinelibrary.wiley.com/doi/10.1111/geb.13346 
> - Gbif https://www.gbif.org/fr/dataset/search?q= 
> - Forest Plots https://forestplots.net/ 
> - CICRA https://www.amazonconservation.org/about/mission-vision/cicra-station/ 

## Informations à extraire

Une première idée serait une classification des différents pixels de l’image selon des classe prédéfinie (à définir avec précision) : Végétation (Forêt, petite végétation, …), Bâtiment, Bitume.

En envisageant l’utilisation d'images hyperspectrales, nous pourrons peut-être récupérer des données plus fines. 
https://www.instadrone.fr/topographie/multispectral/  

Exemples de paramètres :
- estimation de la biomasse, 
- taux de chlorophylle, 
- stress hydrique ou simple imagerie 
- L'NDVI (Indice de Végétation par Différence Normalisée) est un outil d'analyse d'images satellites qui mesure la santé et la densité de la végétation. 
- L’NDWI (indice d'eau par différence normalisée) est utilisé pour détecter les bassins d'eau ouverts sur l'image satellitaire.
- Spectral species is the number of spectrally distinct classes that approximate species. Alpha-diversity and beta-diversity ?

## Prochaines étapes

- Trouver des datasets publiques intéressants pour notre étude.
- Approfondir sur l’utilité des images hyperspectrales dans notre situation.
- Définir les informations à extraire de nos images
