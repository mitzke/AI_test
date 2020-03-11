import numpy as np

rundenanzahl = np.array([0])
print (rundenanzahl)
for i in range (10):
    rundenanzahl = np.append(rundenanzahl, i)
    print (rundenanzahl.mean())