from paciente import Paciente
#Pilar de POO Herança: Idoso herda de Paciente
class Idoso(Paciente):
    def __init__(self, nome, peso, altura):
        super().__init__(nome, peso, altura)
        print("-> Categoria: Idoso adicionado\n")

    #polimorfismo: sobrescrevendo o método calcular_imc da classe Paciente
    def classificar_imc(self):
        imc = self.calcular_imc()       
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso ideal"
        elif 25.0 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"