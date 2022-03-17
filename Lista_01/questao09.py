'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).'''

temperatura_Fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
temperatura_Celsius = 5*((temperatura_Fahrenheit-32)/9)
print(f'Equivale a {temperatura_Celsius} graus Celsius.')