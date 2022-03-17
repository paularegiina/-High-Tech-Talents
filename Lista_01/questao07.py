'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''
import math

lado = float(input("Informe o tamanho da lateral do quadrado: "))
area = (math.pow(lado, 2))
dobro_area = 2*area
print(f'O dobro da sua área: {dobro_area} ')