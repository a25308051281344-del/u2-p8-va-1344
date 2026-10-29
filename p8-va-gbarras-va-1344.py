import numpy as np
import matplotlib.pyplot as plt 
# Adrian Hinojos chavez NC:1344

diasX=["lun","mar","mie","juv","vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("Califas en VA de Adrian Hinojos NC:1344")
plt.xlabel("dias semana habil")
plt.ylabel("Calificaciones en vison artificial")
plt.grid()
plt.show()