from random import randint

class dado: 
    val = 0
    tamaño = 6
    def __init__(self,t = None):
        if t == None: t = dado.tamaño 
        self.tamaño = t
    
    def generarValor(self):
        self.val = randint(1,self.tamaño)