class Retangulo:
  def __init__(self, largura,altura):
    self.largura=largura
    self.altura=altura

  def calcular_area(self):
    return self.altura*self.altura

class Circulo:
    def __init__(self,raio):
      self.raio=raio

    def calcular_area(self):
      return 3.14159*(self.raio**2)

def calcular_area_geometrica(forma):
  return forma.calcular_area()

retangulo = Retangulo(4, 5)
circulo = Circulo(3)

area_retangulo = calcular_area_geometrica(retangulo)
area_circulo = calcular_area_geometrica(circulo)

print("Área do retângulo: ", area_retangulo)
print("Área do Círculo: ", area_circulo)