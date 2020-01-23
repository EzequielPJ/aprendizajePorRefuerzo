import numpy as np
import random
import tkinter as tk

# Inicializa la ventana del mapa que se genera
root = tk.Tk()


class Env():
    def __init__(self):
        self.height = 6  # alto
        self.width = 10  # ancho
        self.posX = 0
        self.posY = 6
        self.endX = self.width - 1
        self.endY = self.height - 1
        self.actions = [0, 1, 2, 3]
        self.stateCount = self.height * self.width
        self.actionCount = len(self.actions)

    def reset(self):
        self.posX = 0
        self.posY = self.height
        self.done = False
        return 0, 0, False

    # Toma la acción y otorga una recompensa al estado correspondiente
    def step(self, action):
        # Selecciona si entre las opciones
        if action == 0:  # left
            if self.posX > 0:
                self.posX = self.posX - 1
            else:
                self.posX
        if action == 1:  # right
            if self.posX < self.width - 1:
                self.posX = self.posX + 1
            else:
                self.posX
        if action == 2:  # up
            if self.posY > 1:
                self.posY = self.posY - 1
            else:
                self.posY
        if action == 3:  # down
            if self.posY < self.height - 1:
                self.posY = self.posY + 1
            else:
                self.posY

        done = self.posX == self.endX and self.posY - 1 == 0
        # mapping (x,y) position to number between 0 and 5x5-1=24
        nextState = self.width * (self.posY - 1) + self.posX

        # Según el estado (casilla) en la que se encuentre gana una recompensa distinta
        if done:
            reward = 100
        else:
            pos = (self.posY - 1) * self.width + self.posX
            reward = self.guardado[pos]
            if reward == 0:
                reward = -30
            if reward == 1:
                reward = 3
            if reward == 2:
                reward = 6
            if reward == 3:
                reward = 9

        return nextState, reward, done

    # devuelbve una acción aleatoria
    def randomAction(self):
        return np.random.choice(self.actions)

    # Se encarga de crear el mapa inicial con el que se trabaja
    def crearMapa(self):
        a = 0
        lista = self.randomLista()
        self.guardado = lista

        x = 0
        y = 0
        while a < self.height * self.width:
            # Calcula la posición respecto de X y Y
            if x < self.width - 1:
                x = x + 1
                if a == 0:
                    x = 0
            else:
                y = y + 1
                x = 0
            board = [[None] * self.width for _ in range(self.height)]
            b = 0
            # Dibuja en la ventana de tkinter el mapa
            for j, row in enumerate(board):
                for i, column in enumerate(row):
                    if self.guardado[b] == 0:
                        lo = tk.Label(root, text='       ', bg='blue', borderwidth=1, relief="solid")
                    elif self.guardado[b] == 1:
                        lo = tk.Label(root, text='       ', bg='brown', borderwidth=1, relief="solid")
                    elif self.guardado[b] == 2:
                        lo = tk.Label(root, text='       ', bg='green', borderwidth=1, relief="solid")
                    elif self.guardado[b] == 3:
                        lo = tk.Label(root, text='       ', bg='grey', borderwidth=1, relief="solid")

                    lo.grid(row=j, column=i)
                    b = b + 1

            # Dibuja el mapa en la consola
            print(self.guardado[a], end='')
            a = a + 1
            if a % self.width == 0:
                print("")

        root.update()
        return self.guardado

    def crearMapaPrueba(self):
        a = 0
        # Una lista que contiene el mapa predetermianado
        lista = [3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 2, 2, 2, 0, 0, 3, 3, 3, 3, 2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 2,
                 1, 1, 1, 2, 3, 3, 3, 3, 3, 2, 2, 1, 0, 0, 0, 0, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0]
        self.guardado = lista
        x = 0
        y = 0
        while a < self.height * self.width:
            if x < self.width - 1:
                # Calcula la posición respecto de X y Y
                x = x + 1
                if a == 0:
                    x = 0
            else:
                y = y + 1
                x = 0
            board = [[None] * self.width for _ in range(self.height)]
            b = 0
            # Dibuja en la ventana de tkinter el mapa
            for j, row in enumerate(board):
                for i, column in enumerate(row):
                    if self.guardado[b] == 0:
                        lo = tk.Label(root, text='       ', bg='blue', borderwidth=1, relief="solid")
                    elif self.guardado[b] == 1:
                        lo = tk.Label(root, text='       ', bg='brown', borderwidth=1, relief="solid")
                    elif self.guardado[b] == 2:
                        lo = tk.Label(root, text='       ', bg='green', borderwidth=1, relief="solid")
                    elif self.guardado[b] == 3:
                        lo = tk.Label(root, text='       ', bg='grey', borderwidth=1, relief="solid")

                    lo.grid(row=j, column=i)
                    b = b + 1

            # Dibuja el mapa en la consola
            print(self.guardado[a], end='')
            a = a + 1
            if a % self.width == 0:
                print("")
        root.update()
        return self.guardado

    # Lo unico que hace es poner una A en el final del recorrido
    def fin(self, epochs):
        posicionAct = ((self.posY - 1) * self.width) + self.posX
        a = 0
        while a < self.height * self.width:
            if a == posicionAct:
                print("A", end='')
                if epochs == 100:
                    lo = tk.Label(root, text='A', borderwidth=1, relief="solid")
                    lo.grid(row=int(self.posY - 1), column=int(self.posX))
                    root.update()
            else:
                print(self.guardado[a], end='')
            a = a + 1
            if a % self.width == 0:
                print("")
        return self.guardado

    # Sirve para generar una lista de numeros que se ponen en el mapa para ver que posiciones
    # valen mas y cuales valen menos
    def randomLista(self):
        size = self.width * self.height
        numbers = [0, 1, 1, 2, 2, 3, 3]
        a = 0
        lista = []
        while a < size:
            if a == 0:
                lista.append(0)
            elif a == size - 1:
                lista.append(0)
            else:
                numeroRandom = random.choice(numbers)
                lista.append(numeroRandom)
            a = a + 1
        return lista

    # Modifica el mapa en cada iteracion
    def modificaMapa(self, epochs):
        # Busca la posicion actual
        posicionAct = ((self.posY - 1) * self.width) + self.posX
        a = 0
        while a < self.height * self.width:
            if a == posicionAct:
                print("A", end='')
                if epochs == 100:
                    lo = tk.Label(root, text='A', borderwidth=1, relief="solid")
                    lo.grid(row=int(self.posY - 1), column=int(self.posX))
                    root.update()
            else:
                print(self.guardado[a], end='')
            a = a + 1
            if a % self.width == 0:
                print("")
        return self.guardado
