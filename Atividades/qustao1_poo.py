class Pessoa:
  def __init__(self,nome,idade):
    self.nome=nome
    self.idade=idade

  def cumprimentar(self):
      return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos "

pessoa1 = Pessoa("João", 30)


mensagem=pessoa1.cumprimentar()
print(mensagem)