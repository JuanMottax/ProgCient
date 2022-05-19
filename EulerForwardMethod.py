##
import numpy as np
import matplotlib.pyplot as plt

a = 0.1
b = 0.2
c = -65
d = 2
i = 14


def ecuacion1(v, u):
    return 0.04 * (v ** 2) + 4 * v + 140 - u + i


def ecuacion2(v, u):
    return a * ((b * v) - u)


def eulerForward(t0, tf, V0, U0):
    h = 0.01
    x = np.arange(t0, tf + h, h)
    V = np.zeros(len(x))
    V[0] = V0
    U = np.zeros(len(x))
    U[0] = U0
    for iter in range(1, len(x)):
        if (V[iter - 1] >= 30):
            V[iter] = c
            U[iter] = U[iter - 1] + d
            continue
        V[iter] = V[iter - 1] + h * ecuacion1(V[iter - 1], U[iter - 1])
        U[iter] = U[iter - 1] + h * ecuacion2(V[iter - 1], U[iter - 1])
    # Graficamos la estimación de Y(t)obtenida
    plt.figure()
    plt.plot(x, U, "r")
    plt.show()
    plt.figure()
    plt.plot(x, V, "r")
    plt.grid(1)
    plt.show()

eulerForward(0, 20, -65, -14)
