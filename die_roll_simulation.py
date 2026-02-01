import matplotlib.pyplot as plt
import numpy as np

def dieRoll(n):
  occurance = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
  for x in range(n):
    roll = np.random.randint(1, 7)
    occurance[roll] += 1
  return occurance

result = dieRoll(10000)
plt.bar(result.keys(), result.values())
plt.show()
print(result)


