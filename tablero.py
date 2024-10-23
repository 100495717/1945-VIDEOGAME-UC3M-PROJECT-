"Creado por Hugo Becerra Fernández, grupo 81 uc3m"
from avion import Avion
from enemigos import Enemigos
from disparos import Disparos
from fondo import Fondo
import pyxel
import random

class Tablero:
    """Esta clase tiene la información necesaria para representar el tablero"""
    def __init__ (self, w: int, h: int):
        self.ancho = w
        self.alto = h

        # Este bloque inicializa pyxel
        #Lo primero que tenemos que hacer es crear la pantalla, ver la API para
        #más parámetros
        pyxel.init(self.ancho,self.alto,title="1942")

        #Cargar el fichero pyxres que vamos a usar
        pyxel.image(2).load(0,0,"assets/avion.png")
        pyxel.image(1).load(0,0,"assets/enemigo11.png")
        pyxel.image(0).load(0,0,"assets/proyedtil.png")
        pyxel.image(1).load(20,20,"assets/enemigo1.png")
        pyxel.image(1).load(36,36,"assets/supermombardero.png")
        pyxel.image(0).load(20,20,"assets/portaviones.png")
        pyxel.image(0).load(200,200,"assets/islote.png")
        self.avion = Avion(self.ancho/2, 200)
        #Clase enemigo
        #self.enemigos = Enemigos(self.ancho/2,1)
        self.enemigos = [Enemigos(random.randint(0,239),1),
                         Enemigos(
            random.randint(0,223),1),Enemigos(random.randint(0,239),1)]
        self.disparos = Disparos(self.ancho/2,200)
        #Creamos una lista para trabajar con los proyectiles
        self.listaproyectiles = []
        #Creamos un "contador" de tiempo para el cooldown
        self.cool_down_count =0
        self.fondo = Fondo(self.ancho/2-30,-500)
        pyxel.run(self.update,self.draw)
    #Creamos una función cooldown para limitar el número de disparos seguidos
    def cooldown (self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1
    def update(self):
        """Esto se ejecuta cada frame, aquí vamos a invocar los métodos
        que actualizan los objetos (update)"""
        self.cooldown()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.avion.move("derecha", self.ancho)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.avion.move("izquierda", self.ancho)
        if pyxel.btn(pyxel.KEY_UP):
            self.avion.move("arriba", self.ancho)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.avion.move("abajo",self.ancho)
        if pyxel.btn(pyxel.KEY_Z) and self.cool_down_count == 0:
                disparo = Disparos(self.avion.x+4, self.avion.y)
                self.listaproyectiles.append(disparo)
                self.cool_down_count = 1
        for i in self.listaproyectiles:
            if i.y < -10:
                self.listaproyectiles.remove(i)
            else:
                i.move()
        self.enemigos[0].move(self.alto,self.ancho)
        self.enemigos[1].move(self.alto, self.ancho-16)
        self.enemigos[2].move(self.alto,self.ancho)
        self.fondo.move(self.alto,self.ancho)

    def draw(self):
        """Esto se ejecuta cada frame, aqui puedo dibujar los objetos
        """
        pyxel.cls(5)

        """Dibujamos el avión tomando los valores del objeto avión 
        Los parámetros son x, y y ua tupla que contiene el banco de 
        imagenes, la x e y inicial y el tamaño de la imagen"""
        pyxel.blt(self.fondo.x, self.fondo.y, *self.fondo.sprite, colkey=0)
        pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite, colkey = 0)
        pyxel.blt(self.enemigos[0].x,self.enemigos[0].y,*self.enemigos[
            0].sprite, colkey = 0)
        pyxel.blt(self.enemigos[1].x, self.enemigos[1].y, *self.enemigos[
            1].sprite, colkey = 0)
        pyxel.blt(self.enemigos[2].x,self.enemigos[2].y,*self.enemigos[
            2].sprite, colkey = 0)
        for i in self.listaproyectiles:
            pyxel.blt(i.x,i.y,*self.disparos.sprite,colkey = 0)