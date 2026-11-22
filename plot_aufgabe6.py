from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DATA_FILE = Path(__file__).with_name("Aufgabe6.txt")
COUNTS_PER_G = 512  # MMA8452Q with SCALE_4G

data = np.loadtxt(DATA_FILE)
if data.ndim != 2 or data.shape[1] != 4:
    raise ValueError("Die Messdatei muss vier Spalten enthalten: X, Y, Z und Zeit in ms.")

time_seconds = (data[:, 3] - data[0, 3]) / 1000
acceleration_g = data[:, :3] / COUNTS_PER_G

plt.figure(figsize=(10, 5))
plt.plot(time_seconds, acceleration_g[:, 0], label="X-Achse")
plt.plot(time_seconds, acceleration_g[:, 1], label="Y-Achse")
plt.plot(time_seconds, acceleration_g[:, 2], label="Z-Achse")
plt.title("Aufgabe 6 – Beschleunigung über die gesamte Messzeit")
plt.xlabel("Zeit [s]")
plt.ylabel("Beschleunigung [g]")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
