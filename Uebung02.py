class Vector3:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def __add__(self, other):
       return Vector3(self.x1 + other.x1, self.x2 + other.x2, self.x3 + other.x3)

    def __sub__(self,other):
       return Vector3(self.x1 - other.x1, self.x2 - other.x2, self.x3 - other.x3)

    def __mul__(self,other):
        if type(other) == int or type(other) == float: #Damit z.B. float und int miteinander addiert werden können
            return Vector3(self.x1 * other, self.x2 * other, self.x3 * other)
        else:
            return Vector3(self.x1 * other.x1, self.x2 * other.x2, self.x3 * other.x3)

    def __rmul__(self,other):
        return Vector3(self.x1 * other, self.x2 * other, self.x3 * other)

    def cross(self,other):
        return Vector3(self.x2*other.x3-self.x3*other.x2,self.x3*other.x1-self.x1*other.x3,self.x1*other.x2-self.x2*other.x1)
    
    def dot(self,other):
        return float(self.x1*other.x1+self.x2*other.x2+self.x3*other.x3) #return mit float, da ja eine Zahl als Resualtat kommt und kein Vektor mehr
 
    def normalize(self):
        return Vector3(round(self.x1/(self.x1**2+self.x2**2+self.x3**2)**0.5,3),round(self.x2/(self.x1**2+self.x2**2+self.x3**2)**0.5,3),round(self.x3/(self.x1**2+self.x2**2+self.x3**2)**0.5,3))

    

v1 = Vector3(4, 2, 4)
v2 = Vector3(3, 2, 1)
v3 = v1*5
v4 = v1.dot(v2)
v5 = v1.normalize()
v6 = v1.cross(v2)
print(f"({v3.x1},{v3.x2},{v3.x3})")
print(v4)  # Zugriff auf das Attribut x1 von v1
print(f"({v5.x1},{v5.x2},{v5.x3})")
print(f"({v6.x1},{v6.x2},{v6.x3})")

