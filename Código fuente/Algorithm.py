from Environment import Env
import numpy as np
import time
import tkinter as tk


# Este método contiene el algoritmo de aprendizaje por refuerzo alterado por nosotros
# Este algoritmo ha sido añadido dentro de un método para llamarlo de forma facil con el Tkinter
def empezar():
    env = Env()
    # Se actualizan las variables con los parametros introducidos en la ventana de Tkinter
    print(valorAncho.get())
    print(valorAlto.get())
    env.width = int(valorAncho.get())
    env.height = int(valorAlto.get())
    env.posY = env.height
    env.endX = int(valorAncho.get()) - 1

    # QTable : contiene los valores Q para cada par (estado, acción)
    qtable = np.random.rand(env.stateCount, env.actionCount).tolist()

    epochs = 100  # Iteraciones que realizará el algoritmo
    gamma = 0.5  # Valor que reduce las rescompensas de forma exponencial según pasan las acciones
    epsilon = 0.1
    decay = 0.1

    print("Mapa inicial")
    # Generamos un mapa aleatoria con los parametros del entrono
    env.crearMapa()

    for i in range(epochs):
        # Reinicia el algoritmo en cada inicio de las iteraciones
        state, reward, done = env.reset()
        steps = 0

        # Mientras que el algoritmo no llegue al estado final propuesto seguimos realizando acciones
        # y cambiando de estado
        while not done:
            print("epoch #", i + 1, "/", epochs)
            time.sleep(0.05)
            # Dibuja la nueva posición de la A en el mapa
            env.modificaMapa(i + 1)
            # Cuenta los pasos realizados hasta llegar el final
            steps += 1

            # Cuando el parametro epsilon es mayor al numero generado automaticamente se realiza una acción
            # aleatoria
            if np.random.uniform() < epsilon:
                action = env.randomAction()
            # Si no selecciona la acción dependiendo de el numero mayor que encontramos en la tabla
            else:
                action = qtable[state].index(max(qtable[state]))

            # Calcula el siguiente estado, la recompensa obtenido y si el algoritmo acabó la iteración
            next_state, reward, done = env.step(action)

            # Hace que la recompensa sea menor en cada iteración
            reward = reward - (steps * 0.5)

            # Si el algoritmo acaba dibuja la A en la posición final
            if done:
                env.fin(i + 1)

            # Muestra el mapa final por Tkinter
            if done and i + 1 == epochs:
                time.sleep(30)
                tk.mainloop()

            # Actualizamos la q-tabla con los valores de la ecuación de bellman
            pos = reward * (gamma ** steps / 2) + 0.9 * max(qtable[next_state])
            qtable[state][action] = pos

            # Actualizamos el estado
            state = next_state
        # Epsilon se reduce en cada iteración para que el algoritmo haga menos elecciones aleatorias
        epsilon -= decay * epsilon

        print("\nDone in", steps, "steps".format(steps))
        time.sleep(0.8)


def empezarPrueba():
    env = Env()
    env.width = 10
    env.height = 6
    env.posY = 6

    # QTable : contiene los valores Q para cada par (estado, acción)
    qtable = np.random.rand(env.stateCount, env.actionCount).tolist()

    epochs = 100  # Iteraciones que realizará el algoritmo
    gamma = 0.8  # Valor que reduce las rescompensas de forma exponencial según pasan las acciones
    epsilon = 0.1
    decay = 0.1

    print("Mapa inicial")
    # Generamos el mapa del problema en concreto
    env.crearMapaPrueba()

    for i in range(epochs):
        # Reinicia el algoritmo en cada inicio de las iteraciones
        state, reward, done = env.reset()
        steps = 0

        # Mientras que el algoritmo no llegue al estado final propuesto seguimos realizando acciones
        # y cambiando de estado
        while not done:
            print("epoch #", i + 1, "/", epochs)
            time.sleep(0.05)
            # Dibuja la nueva posición de la A en el mapa
            env.modificaMapa(i + 1)
            # Cuenta los pasos realizados hasta llegar el final
            steps += 1

            # Cuando el parametro epsilon es mayor al numero generado automaticamente se realiza una acción
            # aleatoria
            if np.random.uniform() < epsilon:
                action = env.randomAction()
            # Si no selecciona la acción dependiendo de el numero mayor que encontramos en la tabla
            else:
                action = qtable[state].index(max(qtable[state]))

            # Calcula el siguiente estado, la recompensa obtenido y si el algoritmo acabó la iteración
            next_state, reward, done = env.step(action)

            # Hace que la recompensa sea menor en cada iteración
            reward = reward - (steps * 0.3)

            # Actualizamos la q-tabla con los valores de la ecuación de bellman
            pos = reward * (gamma ** steps / 2) + 0.9 * max(qtable[next_state])
            qtable[state][action] = pos

            # Si el algoritmo acaba dibuja la A en la posición final
            if done:
                env.fin(i + 1)

            # Muestra el mapa final por Tkinter
            if done and i + 1 == epochs:
                time.sleep(30)
                tk.mainloop()

            # Actualizamos el estado
            state = next_state
        # Epsilon se reduce en cada iteración para que el algoritmo haga menos elecciones aleatorias
        epsilon -= decay * epsilon

        print("\nDone in", steps, "steps".format(steps))
        time.sleep(0.8)


# Crea la ventana para introducir los datos del mapa
ventana = tk.Tk()
ventana.geometry("250x130+100+100")
ventana.title("Creación de mapa")

tk.Label(ventana, text="Introduzca el ancho del mapa:").pack()
entrada = tk.IntVar()
valorAncho = tk.Entry(ventana, textvariable=entrada, width=30)
valorAncho.pack()
tk.Label(ventana, text="Introduzca el alto del mapa:").pack()
entrada2 = tk.IntVar()
valorAlto = tk.Entry(ventana, textvariable=entrada2, width=30)
valorAlto.pack()

tk.Button(ventana, text="Start", command=lambda: empezar()).place(x=100, y=80)
tk.Button(ventana, text="Utilizar el mapa predeterminado", command=lambda: empezarPrueba()).place(x=33, y=110)

ventana.mainloop()
