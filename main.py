
import ast
n=int(input())

class Biblioteka:
  ksiazki=[]
  egzemplarze=[]

class Ksiazka:
    def __init__(self,x):
        self.nazwa=x[0]
        self.autor=x[1]
        self.rok=x[2]
#akcja_dodania_ksiazki_do_biblioteki
    def dodaj(self):
        if str((self.nazwa,self.autor))in egzemplarze.keys():
            egzemplarze[str((self.nazwa,self.autor))]+=1
        else:
            egzemplarze[str((self.nazwa,self.autor))]=1
        return True

class Czytelnik:
    def __init__(self,nazwa,ksiazka):
        self.nazwa=nazwa
        self.ksiazka=ksiazka
#sprawdzenie_mozliwosci_wypozyczenia
    def mozliwosc_wypozyczenia(self):
        if (len(czytelnicy[self.nazwa])<3) and (self.ksiazka not in czytelnicy[self.nazwa]):
            return True
        else:
            return False
#sprawdzenie_czy_ksiazka_dostepna
    def czy_dostepne(self):
        if self.nazwa in czytelnicy.keys():
            return True
        else:
            return False
#akcja wypozyczenia
    def wypozycz(self):
        if self.ksiazka in [eval(x)[0] for x in egzemplarze.keys()]:
            for i,x in egzemplarze.items():
                if eval(i)[0]==self.ksiazka:
                    if egzemplarze[i]>0:
                        egzemplarze[i]-=1
                        czytelnicy[self.nazwa].append(self.ksiazka)
            return True
        else:
            return False
#akcja oddania
    def odddaj(self):
        if self.nazwa in czytelnicy.keys():
            if self.ksiazka in czytelnicy[self.nazwa]:
                czytelnicy[self.nazwa].remove(self.ksiazka)
                for i,x in egzemplarze.items():
                    if eval(i)[0]==self.ksiazka:
                        egzemplarze[i]+=1
            return True
        else:
            return False
        
czytelnicy={}
egzemplarze={}

for i in range(n):
    action=eval(input())
    action = tuple([str(x).strip() for x in action])
    if action[0]=='dodaj':
        print(Ksiazka(action[1:]).dodaj()) 
    if action[0]=='wypozycz':
        if action[1] not in czytelnicy.keys():
            czytelnicy[action[1]]=[]
        if Czytelnik(action[1],action[2]).mozliwosc_wypozyczenia()==False:
            print(Czytelnik(action[1],action[2]).mozliwosc_wypozyczenia())
        else:
            print(Czytelnik(action[1],action[2]).wypozycz())   
    if action[0]=='oddaj':
        print(Czytelnik(action[1],action[2]).odddaj())
