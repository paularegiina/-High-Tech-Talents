'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
import math

raio = float(input("Informe o raio do círculo: "))
area = ( (math.pow(raio, 2)) * math.pi)
print(f'A sua área: {area} ')