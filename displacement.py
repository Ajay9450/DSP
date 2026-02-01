import numpy as np
import matplotlib.pyplot as plt
l = []
def choice(number):
  d = 0
  displace = []
  for a in range(number):
    displace.append(np.random.choice([-1,1]))
  for y in range(len(displace)):
    d += displace[y]
  l.append(d)
  return d,displace


x_axis = []
for x in range(1000):
  x_axis.append(x)
  d , dis = choice(np.random.randint(1,1000000))
  l.append(d)


plt.plot(x_axis,l)
plt.show()
  
