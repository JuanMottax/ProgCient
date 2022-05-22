##
import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 1000
a = 0.02
b = 0.2
c = -50
d = 2
_I = 10
h = 0.5
x = np.arange(t0, tf + h, h)


def IValues(_I):
    I = np.zeros(len(x))
    I[200:1500] = _I
    return I


def ecuacion1(v, u, i):
    return (0.04 * (v ** 2)) + (5 * v) + 140 - u + i


def ecuacion2(v, u):
    return a * ((b * v) - u)


def eulerForward(V0, U0):
    V = np.zeros(len(x))
    V[0] = V0
    U = np.zeros(len(x))
    U[0] = U0
    I = IValues(_I)
    for iter in range(1, len(x)):
        if (V[iter - 1] >= 30):
            V[iter] = c
            U[iter] = U[iter - 1] + d
            V[iter - 1] = 30
        else:
            V[iter] = V[iter - 1] + h * ecuacion1(V[iter - 1], U[iter - 1], I[iter - 1])
            U[iter] = U[iter - 1] + h * ecuacion2(V[iter - 1], U[iter - 1])
    return V, U


def eulerBackward(V0, U0, VFor, UFor):
    V = np.zeros(len(x))
    V[0] = V0
    U = np.zeros(len(x))
    U[0] = U0
    I = IValues(_I)
    for iter in range(1, len(x)):
        if (V[iter - 1] >= 30):
            V[iter] = c
            U[iter] = U[iter - 1] + d
            V[iter - 1] = 30
        else:
            V[iter] = V[iter - 1] + h * ecuacion1(VFor[iter], UFor[iter], I[iter])
            U[iter] = U[iter - 1] + h * ecuacion2(VFor[iter], UFor[iter])
    return V, U


I = IValues(_I)
VFor, UFor = eulerForward(-70, -14)
V, U = eulerBackward(-70, -14, VFor, UFor)
plt.figure()
# plot lines
plt.plot(x, V, label="V")[0]
plt.plot(x, U, label="U")[0]
plt.plot(x, I, label="I")[0]
plt.legend(loc="upper right")
plt.show()

##
