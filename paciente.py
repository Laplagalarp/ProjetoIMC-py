# Abstract: Projeto IMC - Programa para calcular o IMC de um paciente
#classe tem sempre o nome maiusculo
class Paciente:
    #PROPRIEDADES:
    #metodo construtor
    
    def __init__(self, nome, peso, altura):
       
        #pilar do POO encapsulamento
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        print(f"Paciente criado: {self.__nome}")
    # getters
    def get_nome(self):
        return self.__nome

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    # setters
    def set_nome(self):
        return self.__name
    def set_peso(self):
        return self.__peso
    def set_altura(self):
        return self.__altura

    def calcular_imc(self):
        return self.get_peso() / (self.get_altura() ** 2)

    def classificar_imc(self):
        print("Classificar Genérico")

