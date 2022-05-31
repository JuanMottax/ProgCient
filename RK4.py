import numpy as np
import matplotlib.pyplot as plt


def YAnalitic(t):
    # Tasa de infection
    a = 0.5
    # Tasa de recuperación
    b = 0.01
    # Porcentaje inicial de personas susceptibles
    So = 0.99
    # Porcentaje inicial de personas infectadas
    io = 1 - So
    # Total de personas
    N = So + Io
    return ((a*N-b) ((a*N-b)+a*Io(np.exp((a*N-b)*t)-1))



# Definimos la función F(t,y)
# En este caso F depende únicamente de y
def F1(t, y):
    return (0.49 - ((0.00245 * np.exp(0.49 * t)) / (0.49 + 0.005 * (np.exp(0.49 * t) - 1)))) * y
def F1EulerBackMod(t):
    return (0.49 - ((0.00245 * np.exp(0.49 * t)) / (0.49 + 0.005 * (np.exp(0.49 * t) - 1))))

h = 0.01
Y0 = 0.01
T0 = 0.0
Tf = 30.0
T = np.arange(T0, Tf + h, h)
YForEuler = np.zeros(len(T))
YForEuler[0] = Y0
YBackEuler = np.zeros(len(T))
YBackEuler[0] = Y0
YModEuler = np.zeros(len(T))
YModEuler[0] = Y0
YRK2 = np.zeros(len(T))
YRK2[0] = Y0
YRK4 = np.zeros(len(T))
YRK4[0] = Y0
for iter in range(1, len(T)):
  YForEuler[iter] = YForEuler[iter - 1] + h * F1(T[iter - 1], YForEuler[iter - 1])
  YBackEuler[iter] = YBackEuler[iter - 1] / (1 - h * F1EulerBackMod(T[iter]))
  YModEuler[iter] = (YModEuler[iter - 1] + (h / 2) * F1(T[iter - 1], YModEuler[iter - 1])) / (1 - (h / 2) * F1EulerBackMod(T[iter]))

  k1 = F1(T[iter - 1], YRK2[iter - 1])
  k2 = F1(T[iter - 1] + h, YRK2[iter - 1] + k1 * h)
  YRK2[iter] = YRK2[iter - 1] + (h / 2) * (k1 + k2)

  k1 = F1(T[iter - 1], YRK4[iter - 1])
  k2 = F1(T[iter - 1] + 0.5 * h, YRK4[iter - 1] + k1 * 0.5 * h)
  k3 = F1(T[iter - 1] + 0.5 * h, YRK4[iter - 1] + k2 * 0.5 * h)
  k4 = F1(T[iter - 1] + h, YRK4[iter - 1] + k3 * h)
  YRK4[iter] = YRK4[iter - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

plt.figure()
plt.plot(T, YAnalitic(T), 'b')
plt.plot(T, YForEuler, 'r')
plt.plot(T, YBackEuler, 'g')
plt.plot(T, YModEuler, 'm')
plt.plot(T, YRK2, 'y')
plt.plot(T, YRK4, 'maroon')
plt.legend(["Analítica","EulerFor","EulerBack","EulerMod","RK2","RK4"], fontsize=12)
plt.grid(1)
plt.show()