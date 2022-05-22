import ast
n=int(input())


class Biblioteka:
  czytelnicy=[]
  egzemplarze=[]
  wypozyczenia=[]

class Ksiazka:
    def __init__(self,data):
        self.tytul=data[0]
        self.autor=data[1]
        self.rok=data[2]

    def dodaj(self):
        if str((self.tytul, self.autor)) in egzemplarze:
            egzemplarze[str((self.tytul, self.autor))]+=1
        else:
            egzemplarze[str((self.tytul, self.autor))]=1
        return True



class Czytelnik:
    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko

    def __init__(self,tytul,ksiazka):
        self.tytul=tytul
        self.ksiazka=ksiazka

    def czy_dostepne(self):
        if self.tytul in czytelnicy:
            return True
        else:
            return False

    def mozliwosc_wypozyczenia(self):
        if (len(czytelnicy[self.tytul])<3) and (self.ksiazka not in czytelnicy[self.tytul]):
            return True
        else:
            return False
    
    def wypozycz(self):
        if self.ksiazka in [eval(x)[0] for x in egzemplarze]:
            for i,x in egzemplarze.items():
                if eval(i)[0] == self.ksiazka:
                    if egzemplarze[i]>0:
                        egzemplarze[i]-=1
                        czytelnicy[self.tytul].append(self.ksiazka)
            return True
        else:
            return False
    
    def odddaj(self):
        if self.tytul in czytelnicy:
            if self.ksiazka in czytelnicy[self.tytul]:
                czytelnicy[self.tytul].remove(self.ksiazka)
                for i,x in egzemplarze.items():
                    if eval(i)[0] == self.ksiazka:
                        egzemplarze[i]+=1
            return True
        else:
            return False
            


for index in range(0, n):
    input = input().replace('\r', '').replace('\n', '').replace('(', '').replace(')', '').replace(' "', '').replace('"', '').split(",")
    akcja=input[0]



    if akcja[0]=='dodaj':
        print(Ksiazka(akcja[1:]).dodaj())     
    if akcja[0] == 'wypozycz':
        if akcja[1] not in czytelnicy.keys():
            czytelnicy[akcja[1]] = []
        if Czytelnik(akcja[1],akcja[2]).mozliwosc_wypozyczenia() == False:
            print(Czytelnik(akcja[1],akcja[2]).mozliwosc_wypozyczenia())
        else:
            print(Czytelnik(akcja[1],akcja[2]).wypozycz())  
    if akcja[0] == 'oddaj':
        print(Czytelnik(akcja[1],akcja[2]).odddaj())
        
import ast
n=int(input())


class Biblioteka:
  czytelnicy=[]
  egzemplarze=[]
  wypozyczenia=[]

class Ksiazka:
    def __init__(self,data):
        self.tytul=data[0]
        self.autor=data[1]
        self.rok=data[2]

    def dodaj(self):
        if str((self.tytul, self.autor)) in egzemplarze:
            egzemplarze[str((self.tytul, self.autor))]+=1
        else:
            egzemplarze[str((self.tytul, self.autor))]=1
        return True



class Czytelnik:
    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko

    def __init__(self,tytul,ksiazka):
        self.tytul=tytul
        self.ksiazka=ksiazka

    def czy_dostepne(self):
        if self.tytul in czytelnicy:
            return True
        else:
            return False

    def mozliwosc_wypozyczenia(self):
        if (len(czytelnicy[self.tytul])<3) and (self.ksiazka not in czytelnicy[self.tytul]):
            return True
        else:
            return False
    
    def wypozycz(self):
        if self.ksiazka in [eval(x)[0] for x in egzemplarze]:
            for i,x in egzemplarze.items():
                if eval(i)[0] == self.ksiazka:
                    if egzemplarze[i]>0:
                        egzemplarze[i]-=1
                        czytelnicy[self.tytul].append(self.ksiazka)
            return True
        else:
            return False
    
    def odddaj(self):
        if self.tytul in czytelnicy:
            if self.ksiazka in czytelnicy[self.tytul]:
                czytelnicy[self.tytul].remove(self.ksiazka)
                for i,x in egzemplarze.items():
                    if eval(i)[0] == self.ksiazka:
                        egzemplarze[i]+=1
            return True
        else:
            return False
            


for index in range(0, n):
    input = input().replace('\r', '').replace('\n', '').replace('(', '').replace(')', '').replace(' "', '').replace('"', '').split(",")
    akcja=input[0]



    if akcja[0]=='dodaj':
        print(Ksiazka(akcja[1:]).dodaj())     
    if akcja[0] == 'wypozycz':
        if akcja[1] not in czytelnicy.keys():
            czytelnicy[akcja[1]] = []
        if Czytelnik(akcja[1],akcja[2]).mozliwosc_wypozyczenia() == False:
            print(Czytelnik(akcja[1],akcja[2]).mozliwosc_wypozyczenia())
        else:
            print(Czytelnik(akcja[1],akcja[2]).wypozycz())  
    if akcja[0] == 'oddaj':
        print(Czytelnik(akcja[1],akcja[2]).odddaj())
        
