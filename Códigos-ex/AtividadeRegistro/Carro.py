import numpy as np

class Carro():
    def __init__(self, ano, km, modelo) -> None:
        self.ano = ano
        self.km = km
        self.modelo = modelo
        
carros = np.zeros(10, dtype=Carro)

carro1 = Carro(2013, 50000, "Prima")