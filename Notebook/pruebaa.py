import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simular(tablero, generaciones):
    fig, ax = plt.subplots()
    img = ax.imshow(tablero, cmap='binary')

    def actualizar(frame):
        nonlocal tablero
        tablero = actualizar_tablero(tablero)
        img.set_data(tablero)
        return [img]

    ani = animation.FuncAnimation(fig, actualizar, frames=generaciones, interval=300, repeat=False)
    plt.show()
