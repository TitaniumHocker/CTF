import math
import pylab
from matplotlib import mlab

xmin = -1000
xmax = 1000
dx = 0.01
xlist = mlab.frange(xmin, xmax, dx)

file = open("q95.txt", "r")
f = file.read().replace("\n", "").split(",")
f.remove("")
y = []
x = []

for i in range(len(f)):
    f[i] = int(f[i].strip())
    if i % 2 == 0:
        x.append(f[i])
    else:
        y.append(f[i])



print(f)
print("------------------")
pylab.plot(y, x)
pylab.show()
