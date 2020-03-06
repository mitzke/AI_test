import random
class Macke(object):
    def __init__ (self, anzahlwuerfel=6, value=0, ergebnis=0,):
        self.anzahlwuerfel = anzahlwuerfel
        self.ergenis = ergebnis
        self.value = value
    def wuerfeln (self):
        self.ergebnis = sorted([random.randint(1, 6) for i in range(self.anzahlwuerfel)])
        #print (self.ergebnis)
        return self.ergebnis
    
    def dreigleiche (self, zahl):
            anzahl = self.ergebnis.count(zahl)
            if anzahl == 3:
                return zahl
            else:
                return 0
    def viergleiche (self, zahl):
            anzahl = self.ergebnis.count(zahl)
            if anzahl == 4:
                return zahl
            else:
                return 0
    def fuenfgleiche (self, zahl):
            anzahl = self.ergebnis.count(zahl)
            if anzahl == 5:
                return zahl
            else:
                return 0
    def einser (self):
        anzahl1 = self.ergebnis.count(1)
        if anzahl1 == 1:
            return 1
        elif anzahl1 == 2:
            return 2
        else:
            return 0
        
    def fuenfer (self):
        anzahl5 = self.ergebnis.count(5)
        if anzahl5 == 1:
            return 1
        elif anzahl5 == 2:
            return 2
        else:
            return 0       
    def strasse (self):
        street = [1, 2, 3, 4, 5, 6]
        if self.ergebnis == street:
            print ("Straße - alle wieder rein")
            return 1
        else:
            return 0
    def punkte (self): 
        value_int = 0
        ## Check auf drei gleiche
        for i in range(2,7):
            D = self.dreigleiche(i)*100
            value_int += D
        for i in range(2,7):
            D = self.viergleiche(i)*200
            value_int += D
        for i in range(2,7):
            D = self.fuenfgleiche(i)*400
            value_int += D
        ##gleiche 1er
        value_int += self.dreigleiche(1)*1000
        value_int += self.viergleiche(1)*2000
        value_int += self.fuenfgleiche(1)*4000
  
        ##Check auf 1er und 5er      
        value_int += self.einser()*100
        value_int += self.fuenfer()*50
        ##Check auf Straße
        value_int += self.strasse()*1000
        
        ########################################################################
        ##Check auf Macke auf Schuss  TODO
        ########################################################################
        
        if value_int == 0:
            return 0
        else:
            self.value += value_int
            return self.value
        
    def weiterwuerfeln(self):
        ## 1er raus
        for i in range (self.anzahlwuerfel):
            if 1 in self.ergebnis:
                self.ergebnis == self.ergebnis.remove(1)
        ##5er raus
        for i in range (self.anzahlwuerfel):
            if 5 in self.ergebnis:
                self.ergebnis == self.ergebnis.remove(5)
        ##Gleiche raus
        for i in range (2,7):
            if self.dreigleiche(i) != 0:
                for p in range (3):
                    self.ergebnis == self.ergebnis.remove(i)
            if self.viergleiche(i) != 0:
                for p in range (3):
                    self.ergebnis == self.ergebnis.remove(i)
            if self.fuenfgleiche(i) != 0:
                for p in range (3):
                    self.ergebnis == self.ergebnis.remove(i)
        L = len(self.ergebnis)
        if L > 0:
            self.anzahlwuerfel = L
        else:
            print("Alle wieder rein")
            self.anzahlwuerfel = 6
        return self.ergebnis
        return self.anzahlwuerfel
W1 = Macke()
anz_wuerf = 0
for i in range (1):
    P = 1
    while P > 0:
        anz_wuerf += 1
        Wurf = W1.wuerfeln()
        print(Wurf)
        P = W1.punkte()
        print(P)
        W1.weiterwuerfeln()
        if P > 0:
            PZ = P
    else:
        print ("MACKE")
    print ("es wurde {} mal gewürfelt".format(anz_wuerf))
    print ("Höchstpunktzahl {}".format(PZ))
    print ("Der letzte Wurf war {}".format(Wurf))
    print ("Es blieben {} Wuerfel uebrig".format(len(Wurf)))
