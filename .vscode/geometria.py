class Retangulo:
    def __init__(self,base,altura) :
        self.base = base
        self.altura = altura

    def area(self) :
        return self.base * self.altura

    def perimetro(self) :
        return (self.base * 2) + (self.altura*2)

        

Retangulo1 = Retangulo(5,3)
area1 = Retangulo1.area()
perimetro1 = Retangulo1.perimetro()

print(f"Area é de {area1}")
print (f"Perimetro é de {perimetro1}")