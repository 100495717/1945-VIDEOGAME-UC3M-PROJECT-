"Creado por Hugo Becerra Fernández, grupo 81 uc3m"
class Disparos:
    def __init__(self, x,y):
        self.sprite = (0,0,0,15,15)
        self.x = x
        self.y = y
    def move(self):
        self.y  -=10
