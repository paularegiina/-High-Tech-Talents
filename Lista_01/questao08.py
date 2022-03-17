'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
valor_hora = float(input("Informe seu valor hora-trabalho: "))
qtd_hora = float(input("Informe a quantidade de horas trabalhadas: "))
salario = valor_hora*qtd_hora
print(f'Salario do mês: {salario} ')