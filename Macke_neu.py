import random
import numpy as np


def wuerfeln (anzahl_wuerfel):
    wurf = sorted([random.randint(1, 6) for i in range(anzahl_wuerfel)])
    print (wurf)
    points, wurf_neu = punkte(wurf)
    return points, wurf_neu

def dreigleiche (wurf, zahl):
    anzahl = wurf.count(zahl)
    if anzahl == 3:
        #print (wurf)
        for i in range(3):
            wurf.remove(zahl)
        return zahl, wurf
    else:
        return 0, wurf

def viergleiche (wurf, zahl):
    anzahl = wurf.count(zahl)
    if anzahl == 4:
        #print (wurf)
        for i in range(4):
            wurf.remove(zahl)
        return zahl, wurf
    else:
        return 0, wurf

def fuenfgleiche (wurf, zahl):
    anzahl = wurf.count(zahl)
    if anzahl == 5:
        #print (wurf)
        for i in range(5):
            wurf.remove(zahl)
        return zahl, wurf
    else:
        return 0, wurf

def einser (wurf):
    anzahl1 = wurf.count(1)
    if anzahl1 in range (1,3):
        for i in range (anzahl1):
            wurf.remove(1)
        return anzahl1, wurf
    else:
        return 0, wurf
    
def fuenfer (wurf):
    anzahl5 = wurf.count(5)
    if anzahl5 in range (1,3):
        for i in range (anzahl5):
            wurf.remove(5)
        return anzahl5, wurf
    else:
        return 0, wurf     
def strasse (self):
    street = [1, 2, 3, 4, 5, 6]
    if self.ergebnis == street:
        print ("Straße - alle wieder rein")
        return 1
    else:
        return 0
def punkte (wurf):
    wurf_neu = []
    Gesamtpunkte = 0
    ## Check auf drei gleiche
    for i in range(2,7):
        punkte, wurf_neu = dreigleiche(wurf, i)  
        Gesamtpunkte += 100*punkte
    for i in range(2,7):
        punkte, wurf_neu = viergleiche(wurf, i)  
        Gesamtpunkte += 200*punkte
    for i in range(2,7):
        punkte, wurf_neu = fuenfgleiche(wurf, i)  
        Gesamtpunkte += 300*punkte
    ## check auf 1000
    punkte1000, wurf_neu = dreigleiche(wurf, 1)  
    Gesamtpunkte += 1000*punkte1000
    punkte2000, wurf_neu = viergleiche(wurf, 1)  
    Gesamtpunkte += 2000*punkte2000
    punkte3000, wurf_neu = fuenfgleiche(wurf, 1)  
    Gesamtpunkte += 3000*punkte3000
    ## Check auf 1er und 5er
    punkte1, wurf_neu = einser(wurf_neu)
    Gesamtpunkte += punkte1*100
    punkte5, wurf_neu = fuenfer(wurf_neu)
    Gesamtpunkte += punkte5*50

    ########################################################################
    ##Check auf Macke auf Schuss  TODO
    ########################################################################
    print ("Wurfpunkte",Gesamtpunkte)
    print ("Restwuerfel",wurf_neu)
    return Gesamtpunkte, wurf_neu

def weiterwuerfeln(anzahl_restwuerfel):
    wurf = sorted([random.randint(1, 6) for i in range(anzahl_restwuerfel)])
    print (wurf)
    points, wurf_neu = punkte(wurf)
    return points, wurf_neu

#    wurfzahl = 1
#for i in range(1000):
#    Gesamtpunkte = 0
#    points, wurf_neu = wuerfeln(5)
#    Gesamtpunkte += points
#    while points>0 and len(wurf_neu)>0:
#        wurfzahl += 1
#        points, wurf_neu = wuerfeln(len(wurf_neu))
#        Gesamtpunkte += points
#        print("Zwischenstand:",Gesamtpunkte)
#        if points>0 and len(wurf_neu)==0:
#            print("alle wieder rein")
#            points, wurf_neu = wuerfeln(5)
#            Gesamtpunkte += points
#    print ("Macke! Höchstpunktzahl",Gesamtpunkte, "Anzahl wuerfe",wurfzahl)
    

