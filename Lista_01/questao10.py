'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit..'''

temperatura_Celsius = float(input("Informe a temperatura em graus Celsius: "))
temperatura_Fahrenheit = (((9*temperatura_Celsius)/5) + 32)
print(f'Equivale a {temperatura_Fahrenheit} graus Fahrenheit.')