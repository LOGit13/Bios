import os
import matplotlib.pyplot as plt
import numpy as np


datei_pfad = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "Aufgabe6.txt")
)
counts_pro_g = 512

messdaten = np.loadtxt(datei_pfad)
if messdaten.ndim != 2 or messdaten.shape[1] != 4:
    raise ValueError("Die Messdatei muss vier Spalten enthalten: X, Y, Z und Zeit in ms.")

zeit_sekunden = (messdaten[:, 3] - messdaten[0, 3]) / 1000
beschleunigung_g = messdaten[:, :3] / counts_pro_g

plt.figure(figsize=(10, 5))
plt.plot(zeit_sekunden, beschleunigung_g[:, 0], label="X-Achse")
plt.plot(zeit_sekunden, beschleunigung_g[:, 1], label="Y-Achse")
plt.plot(zeit_sekunden, beschleunigung_g[:, 2], label="Z-Achse")
plt.title("Aufgabe 6 – Beschleunigung über die gesamte Messzeit")
plt.xlabel("Zeit [s]")
plt.ylabel("Beschleunigung [g]")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
