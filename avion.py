"Creado por Hugo Becerra Fernández, grupo 81 uc3m"
class Avion:
    """Esta clase almacena toda la información necesaria para nuestro avión"""
    """Es muy probable que encesitemos más atributos, aquí mostramos los 
    básicos"""

    def __init__(self,x:int,y:int):
        """Este método crea el objeto avión
        @param x la x inicial
        @param la y inicial
        """
        self.x = x
        self.y = y

        #Aquí asumimos que la imagen del avión estará en el primer banco en
        #la primera posición y tendrá 16x16 de tamaño
        self.sprite = (2,0,0,40,40)
        #Consideramos que tiene tres vidas al principio del juego
        self.vidas = 3

    def move(self, direccion:str,tamaño:int):
        """Esto es un ejemplo de un método que mueve el Avión,
        recibe la dirección y el tamaño del tablero"""
        tamaño_avion_x = self.sprite[3]
        tamaño_avion_y = self.sprite[3]
        if direccion.lower() == "derecha" and self.x <tamaño \
                - tamaño_avion_x:
            self.x += 3
        if (direccion.lower() == "izquierda") and self.x > 0:
            self.x-=3
        if direccion.lower() == "arriba" and self.y >0:
            self.y -=3
        if direccion.lower() == "abajo" and self.y< tamaño-tamaño_avion_y:
            self.y += 3
