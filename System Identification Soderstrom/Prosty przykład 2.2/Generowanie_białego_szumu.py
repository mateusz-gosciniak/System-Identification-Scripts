import numpy as np
import pylab as pl


def normal_distribution(sigma, mi):
  x = np.linspace(-3, 3, N)
  return 1 / ( sigma * np.sqrt(2 * np.pi) ) * np.exp ( -(x - mi)**2 / (2 * sigma**2) )


def variance(x, expected_value):
  n = len(x)
  sum = 0
  for i in range(n):
    sum += (x[i] - expected_value)**2
  return sum/n


def expected_value(x):
  return np.sum(x)/len(x)


#---------------------------------------------------------

N = 1000
sigma = 1
mi = 0
x = np.linspace(-3, 3, N)
y = normal_distribution(sigma, mi)

pl.title("standardowy rozkład normalny - PDF")
pl.xlabel("x")
pl.ylabel("N(mi, sigma) [mi = 0, sigma = 1]")
pl.grid()
pl.plot(x, y)
pl.show()

#---------------------------------------------------------

N = 10**5
x = np.linspace(-1, 1, N)
r = np.random.normal(size=N)

pl.plot(x, r)
pl.show()

pl.hist(r, 100, color='g', edgecolor='black')
pl.show()

pl.plot(x, np.sort(r))
pl.show()

Ex = expected_value(r)
print("expected value: " + str(Ex) + "; should be equal to 0")
print("variance: " + str(variance(r ,Ex)) + "should be equal to 1")
print("median: " + str(np.median(r)))
print("mean: " + str(np.mean(r)))

#---------------------------------------------------------

