#lobby clinica
from adulto import Adulto
from idoso import Idoso

print("Bem-vindo(a) à clínica de saúde!\n")
paciente1 = Adulto("Sofia", 43, 1.53)
paciente2 = Idoso("Arthur", 70, 1.70)
print("RELATÓRIO DE PACIENTES\n")
lista_pacientes = [paciente1, paciente2]
for paciente in lista_pacientes:
    imc = paciente.calcular_imc()
    classificacao = paciente.classificar_imc()
    print(f"Nome: {paciente.get_nome()}")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}\n")