from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DATA_FILE = Path(__file__).with_name("Aufgabe5.txt")
COUNTS_PER_G = 512  # MMA8452Q with SCALE_4G
PLOT_DURATION_SECONDS = 4

data = np.loadtxt(DATA_FILE)
if data.ndim != 2 or data.shape[1] != 4:
    raise ValueError("Die Messdatei muss vier Spalten enthalten: X, Y, Z und Zeit in ms.")

time_seconds = (data[:, 3] - data[0, 3]) / 1000
first_four_seconds = time_seconds <= PLOT_DURATION_SECONDS

time_seconds = time_seconds[first_four_seconds]
acceleration_g = data[first_four_seconds, :3] / COUNTS_PER_G

plt.figure(figsize=(10, 5))
plt.plot(time_seconds, acceleration_g[:, 0], label="X-Achse")
plt.plot(time_seconds, acceleration_g[:, 1], label="Y-Achse")
plt.plot(time_seconds, acceleration_g[:, 2], label="Z-Achse")
plt.title("Beschleunigungssensor – erste 4 Sekunden")
plt.xlabel("Zeit [s]")
plt.ylabel("Beschleunigung [g]")
plt.xlim(0, PLOT_DURATION_SECONDS)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
