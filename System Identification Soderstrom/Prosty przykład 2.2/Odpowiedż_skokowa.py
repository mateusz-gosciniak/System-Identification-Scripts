import numpy as np
import pylab as pl

N = 100 # ilość próbek
t_start = 0
t0 = 10 # pobudzenie w chwili t = 10s
t_end = 100
t = np.linspace(t_start,t_end,N) #time [s] - oś x
e = np.random.normal(size=N) # szum biały jako zakłucenie e(t) 
u1 = np.zeros(t_start + t0)
u2 = np.linspace(0,t_end,N - len(u1))
u = [*np.zeros(t_start + t0), *np.linspace(0,t_end,N - len(u1))] # funkcja wejściowa
x = np.zeros(N)

x[0] = 0
for i in range(1, N):
    div = (u[i] - 0.8 * u[i-1])
    if div != 0:
        x[i] = u[i-1] / div
    else:
       x[i] = 0

y = np.zeros(N)
for i in range(N):
    y[i] = x[i] + e[i]


pl.title("Odpowiedź skokowa")
pl.grid()
pl.plot(t, x)
pl.plot(t, y)
pl.show()