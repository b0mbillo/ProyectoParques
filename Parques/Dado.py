from random import randint

class Dado: 
    val = 0
    tamaño = 6
    def __init__(self,t = None):
        if t == None: t = Dado.tamaño 
        self.tamaño = t
    
    def generarValor(self):
        self.val = randint(1,self.tamaño)