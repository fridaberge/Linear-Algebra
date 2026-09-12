from random import randint
from Kort import Kort

#lager en kortstokk med alle kortene
def lagKortstokkSortert(typeKort):
    kortstokkSortert = [Kort for i in range(52)]
    indeks = 0
    for i in range(4):
        for j in range(13):
            kort = Kort(j+1,typeKort[i])
            kortstokkSortert[indeks] = kort
            indeks +=1
    return kortstokkSortert

#stokker en sortert kortstokk
def stokkKort(sortert):
    kortStokket = [Kort for i in range(52)]
    i=0
    while len(sortert) > 0:
        kort = sortert.pop(randint(0,len(sortert)-1))
        kortStokket[i] = kort
        i +=1
    return kortStokket

#legger kortet på bordet
def leggKort(stokk, kort, bunker, neste):

    #finner ut om man skal hoppe over bunken eller legge ned
    runde = 0
    while(bunker[neste-1][0] != None) and (bunker[neste-1][0].tall == neste):
        #hvis man må gå rundt hele klokka for å legge et kort har kabalen gått opp
        if runde>13:
            return -1
        runde += 1
        if neste == 13:
            neste = 1
        else:
            neste += 1

    #hvis kortet legges riktig sted (eks. A på 1)
    bunke = bunker[neste-1]
    if(neste == kort.tall):
        if(bunke[0] != None):
            for l in range(len(bunke)):
                stokk.append(bunke[l])

            for i in range(len(bunke)):
                bunker[neste-1].pop(0)
        nyBunke = []
        nyBunke.append(kort)
        bunker[neste-1] = nyBunke
    #hvis kortet legges på en annen bunke enn sin egen (eks. A på 2)
    else:
        if(bunke[0] == None):
            bunke[0] = kort
        else:
            bunke.append(kort)

    if(neste <= 12):
            neste +=1 
    else:
        neste = 1
    return neste


def hendelseslokke(stokk, bunker):
    neste = 1
    #trekker øverste(på plass 0) kort fra bunken helt til det ikke er fler kort eller kabalen går opp
    while len(stokk) > 0:
        kort = stokk.pop(0) 
        neste = leggKort(stokk, kort, bunker, neste)
        if(neste == -1):
            #returnerer 1 ved suksess
            return 1
    #returnerer -1 ved fiasko, altså når neste er mellom 1 og 13 og alle kortene lagt
    return -1 
        


#Ble brukt til feilsøking
def printBunker(bunker):
    print("Klokka:")
    for i in range(13):
        bunke = bunker[i]
        for j in range(len(bunke)):
            print("Bunke", i+1,":", bunke[j])


#selve programmet som legger kabalen og beregner sannsynligheten
def main():
    typeKort = ["Hjerter", "Kløver", "Ruter", "Spar"]
    a = 0 #antall som gikk opp
    b = 0 #antall som ikke gikk opp
    antTotal = input("Hvor mange kabaler vil du legge? ")

    for i in range(int(antTotal)):
        bunker = [[None for i in range(1)] for j in range(13)]
        sortertStokk = lagKortstokkSortert(typeKort)
        stokketStokk = stokkKort(sortertStokk)
        gikkOpp = hendelseslokke(stokketStokk, bunker)
        if(gikkOpp == 1):
            a+=1
        elif (gikkOpp == -1):
            b+=1
    brok = round(a/(a+b), 3)
    print("\n\nTotalt antall kabaler lagt: ", antTotal,"\nAntall som gikk opp: ", a, "\nAntall som ikke gikk opp: ", b, "\nSannsynlighet for suksess a/(a+b): ", brok)

main()
