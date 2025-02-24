class Info:
  def __init__(self, idade, altura, peso):
    self.idade = idade
    self.altura = altura
    self.peso = peso
  
  def show_info(self):
    return {
      "idade": self.idade,
      "altura": self.altura,
      "peso" : self.peso
    }

pessoa = Info(15, 1.62, 70)