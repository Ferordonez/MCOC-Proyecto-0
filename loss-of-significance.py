import numpy as np
from matplotlib import pyplot

#Volumen de un cilindro
R = 1 #radio fijo 
h = 4 #altura inicial (variable)


f64=[h] #lista de tamañofloat64
f32=[h] #lista de tamaño float32

for i in range(5): #Tomamos una rango de 5 numeros de variacion
    alt=(f64[-1])
    Vol1 = (R**2)*3.14*alt 
    f64.append(np.float64(Vol1))
    
    altu=(f32[-1])
    Vol2 = (R**2)*3.14*altu
    f32.append(np.float32(Vol2))
    
    
print f64[-1]
print f32[-1]
error = []

for i in range(len(f32)):
    error.append((abs(f64[i]-f32[i])))
pyplot.plot(error)

for i in range(5):  #imprimimos el recorrido de los 5 numeros
    print "Alt_f32:",f32[i],"Alt_f64:",f64[i],"Error:", error[i]
