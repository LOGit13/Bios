import os
import matplotlib.pyplot as plt
import numpy as np

# Letzte vier Sekunden der Messung 
datei_pfad = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "Aufgabe4.txt")
)
messdaten = np.loadtxt(datei_pfad)
startzeit_ms = messdaten[-1, 3] - 4000
messdaten = messdaten[messdaten[:, 3] >= startzeit_ms]

x = messdaten[:, 0] / 1024
y = messdaten[:, 1] / 1024
z = messdaten[:, 2] / 1024
t = (messdaten[:, 3] - startzeit_ms) / 1000

# Plot
plt.figure(figsize=(10,5))

plt.plot(t, x, marker='o', label='X-Achse')
plt.plot(t, y, marker='o', label='Y-Achse')
plt.plot(t, z, marker='o', label='Z-Achse')

plt.title('Beschleunigungssensor - 4 Sekunden Messung')
plt.xlabel('Zeit [s]')
plt.ylabel('Beschleunigung [g]')
plt.legend(loc='lower right')
plt.grid(True)
plt.xlim(0, 4)

plt.show()