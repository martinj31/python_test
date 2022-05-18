import csv
import json

resultDepartement = {}
resultRegion = {}

with open('data/people.csv', newline='') as f:
    readerPersonne = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for personne in readerPersonne: 
        with open('data/lieux.csv', newline='') as f:
            readerLieu = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            #Lecture personne
            for lieu in readerLieu:#Lecture Lieu
                #regarde si la personne est née dans ce lieu (commune)     
                
                if lieu[1] == "departement" :
                    continue
                
                if personne[3] == lieu[0] :
                   
                #regarde si le lieu (departement) a deja etait vu
                    if lieu[1] in resultDepartement: 
                        #prend le nombre de personne née et ajoute 1
                        nee = resultDepartement.get(lieu[1]) 
                        nee += 1         
                        resultDepartement[lieu[1]] = nee

                    else :
                        resultDepartement[lieu[1]] = 1


                    #regarde si le lieu (departement) a deja etait vu
                    if lieu[2] in resultRegion: 
                     #prend le nombre de personne née et ajoute 1
                        nee = resultRegion.get(lieu[2]) 
                        nee += 1         
                        resultRegion[lieu[2]] = nee

                    else :
                        resultRegion[lieu[2]] = 1 
            
with open('resultRegion.json', 'w', encoding='utf-8') as f:
    json.dump(resultRegion, f, ensure_ascii=False, indent=2)

with open('resultDepartement.json', 'w', encoding='utf-8') as f:
    json.dump(resultDepartement, f, ensure_ascii=False, indent=2)

print(resultRegion)    
print(resultDepartement)  
