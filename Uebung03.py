import math

#---------------------------------

class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#----------------------------------

class Figur:
    def __init__(self, name):
        self.name = name

    def umfang(self): 
        return 0 
    
    def __str__(self): 
        return self.name 

#---------------------------------
    
class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.m = mittelpunkt
        self.r = radius

    def umfang(self):
        if self.r == 0:
            print("radius = 0 und somit keinen Umfang -> Ihre Eingabe:") 
        else:
            return self.r*math.pi*2
    
    def __str__(self):
        return f"Objekt = {self.name}, Mittelpunkt = ({self.m.x}/{self.m.y}), Radius = {self.r}"

    
#----------------------------------

class Dreieck(Figur):
    def __init__(self, PunktA, PunktB, PunktC):
        super().__init__("Dreieck")
        self.a = PunktA 
        self.b = PunktB 
        self.c = PunktC

    def umfang(self):
        AB = math.sqrt((self.a.x - self.b.x)**2+(self.a.y-self.b.y)**2)
        BC = math.sqrt((self.b.x - self.c.x)**2+(self.b.y-self.c.y)**2)
        CA = math.sqrt((self.c.x - self.a.x)**2+(self.c.y-self.a.y)**2)
        if AB == 0 and BC == 0 and CA == 0:
            print("Es handelt sich um einen Punkt, Koordniaten identisch -> Ihre Eingabe:")
        elif AB == 0 or BC == 0 or CA == 0 or self.a.x == self.b.x == self.c.x or self.a.y == self.b.y == self.c.y:
            print("Es handelt sich um eine Linie, nicht um ein Dreieck -> Ihre Eingabe:")
        else:
            return AB + BC + CA
        
    def __str__(self):
        return f"Objekt = {self.name}, Punkt A = ({self.a.x}/{self.a.y}), Punkt B = ({self.b.x}/{self.b.y}), Punkt C = ({self.c.x}/{self.c.y})"
    
#------------------------------------
    
class Rechteck(Figur):
    def __init__(self, PunktA,PunktD):
        super().__init__("Rechteck")
        self.a = PunktA
        self.d = PunktD

    def umfang(self):
        a = abs(self.a.x - self.d.x)
        b = abs(self.a.y - self.d.y)
        if a == 0 and b == 0:
            print("Es handelt sich um einen Punkt, Koordniaten identisch -> Ihre Eingabe:")
        elif a == 0 or b == 0:
            print("Es handelt sich um eine Linie, nicht um ein Rechteck -> Ihre Eingabe:")
        else:
            return 2*(a+b)

    def __str__(self):
        return f"Objekt = {self.name}, Punkt A = ({self.a.x}/{self.a.y}), Punkt D (diagonal von Punkt A) = ({self.d.x}/{self.d.y})"
    
#--------------------------------
  

class Polygon(Figur):
    def __init__(self, punkte):
        super().__init__("Polygon")
        self.punkte = punkte #Punkte als Liste

 # Lösung Chatgpt 

    def umfang(self):
        u = 0
        for i in range(len(self.punkte)):
            j = i + 1
            if j > len(self.punkte)-1:
                j = 0

        u = u + math.sqrt((self.punkte[i].x - self.punkte[j].x)**2 + 
                          (self.punkte[i].y - self.punkte[j].y)**2)

        return u


 # Lösung Chatgpt 

    #def __str__(self):
        #punkte_str = ", ".join([f"({punkt.x}/{punkt.y})" for punkt in self.punkte]) #<- Funktion, die mittels join die einzelnen Punkte zusammenfügt.
        #return f"Objekt = {self.name}, Punkte = ({punkte_str})"
    
    def __str__(self):
        list = []
        for punkt in self.punkte:
            list.append(f"({punkt.x}/{punkt.y})")
        return f"Objekt = {p.name}, Punkte = {list}"

        
#------------------------------------


k = Kreis(Punkt(0,0),5)
print(k.name,k.umfang())
print(k)

d = Dreieck(Punkt(1,1),Punkt(5,1),Punkt(3,2))
print(d.name,d.umfang())
print(d)

r = Rechteck(Punkt(1,5),Punkt(5,2))
print(r.name,r.umfang())
print(r)

punkte = [Punkt(0, 0), Punkt(1, 0), Punkt(1, 1), Punkt(0, 1)]
p = Polygon(punkte)
print(p.name,p.umfang())
print(p)