from random import randint

class Dado: 
    tamañoDefault = 6
    def __init__(self,t = None):
        if t is None: t = Dado.tamañoDefault 
        self.tamaño = t
        self.val = 0
    
    def generarValor(self):
        self.val = randint(1,self.tamañoDefault)