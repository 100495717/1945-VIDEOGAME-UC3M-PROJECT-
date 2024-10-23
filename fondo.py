#Creado por Hugo Becerra Fernández
class Fondo:
    def __init__(self, x,y):
        self.sprite = (0,20,20,80,182)
        self.x = x
        self.y = y
    def move(self,x,y):
        self.Porta = False
        self.isla1 = False
        if self.y < 500:
            self.y+= 3

        if self.y >= 500:
            self.Porta = True
        if self.y >= 500 and self.Porta == True:
            self.sprite = (0,200,200,1000,1000)
            self.y = -500




