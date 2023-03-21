# Machine: lscpu

Voici le résultat de la commande `lscpu` <br/>

Architecture :                              x86_64<br/>
  Mode(s) opératoire(s) des processeurs :   32-bit, 64-bit<br/>
  Address sizes:                            48 bits physical, 48 bits virtual<br/>
  Boutisme :                                Little Endian<br/>
Processeur(s) :                             16<br/>
  Liste de processeur(s) en ligne :         0-15<br/>
Identifiant constructeur :                  AuthenticAMD<br/>
  Nom de modèle :                           AMD Ryzen 7 4800H with Radeon Graphi<br/>
                                            cs
    Famille de processeur :                 23<br/>
    Modèle :                                96<br/>
    Thread(s) par cœur :                    2<br/>
    Cœur(s) par socket :                    8<br/>
    Socket(s) :                             1<br/>

Ainsi ma machine possède 4 coeurs logiques et 8 coeurs logiques 

Voici la quantité de mémoire L2 et L3 de ma machine
Caches (sum of all):                        
  L2:                                       4 MiB (8 instances)
  L3:                                       8 MiB (2 instances)


# Automate cellulaire 1D

Pour calculer le speed up on va prendre le temps total c'est à dire : Temps de calcul + Temps d'affichage


|Nombre de process|Temps totale (s)|Speed up|
|-|-|-|
|1|	8,010815	|1 |
|2|	4,004604	|2,000401288 |
|3|	2,753906	|2,908891952 |
|4|	2,091147	|3,830823467 |
|5|	1,674589	|4,783749923 |
|6|	1,380992	|5,800768578 |
|7|	1,1525759|	6,95035789 |
|8|	1,0855906|	7,379222886 |
		
Voila ce que donne le graphe
<br/>

![Graphe]( graphe.png "a title")

# Calcul d'une enveloppe convexe

