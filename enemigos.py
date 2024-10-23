"Creado por Hugo Becerra Fernández, grupo 81 uc3m"
import pyxel
import random
class Enemigos:
    def __init__ (self, x:int,y:int):
        self.x=x
        self.y=y
        self.sprite = (1, 0, 0, 16, 16)



    def move(self,x,y):
        self.primer_sprite = True
        if self.primer_sprite and self.sprite == (1,0,0,16,16) and self.y < \
                400/2:
            self.y += (2)
            if self.y >= 400 / 2:
                self.sprite = (1, 20, 20, 28, 28)
                self.y = 400/2
        if self.sprite == (1,20,20,28,28) and self.y <=400/2:
            self.y -=2
        if self.x <= 400 - 16 and self.x > 16 and self.y <= 400/3:
            self.x -=2
        if self.x <= 400 - 16 and self.x > 16 and self.y <= 400/2:
            self.x += 2
        if self.y <=0:
            self.sprite = (1,40,40,203,127)
            self.y = 350
            self.x = 245
        if self.sprite == (1,40,40,203,127):
            self.y -=2
        if self.sprite == (1,40,40,203,127) and self.y<=0:
            self.sprite = (1, 0, 0, 16, 16)
            self.y = 0
            if self.primer_sprite and self.sprite == (
            1, 0, 0, 16, 16) and self.y < \
                    400 / 2:
                self.y += (2)
                if self.y >= 400 / 2:
                    self.sprite = (1, 20, 20, 28, 28)
                    self.y = 400 / 2
            if self.sprite == (1, 20, 20, 28, 28) and self.y <= 400 / 2:
                self.y -= 2
            if self.x <= 400 - 16 and self.x > 16 and self.y <= 400 / 3:
                self.x -= 2
            if self.x <= 400 - 16 and self.x > 16 and self.y <= 400 / 2:
                self.x += 2




