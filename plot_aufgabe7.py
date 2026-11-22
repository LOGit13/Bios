from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

DATA_FILE = Path(__file__).with_name("Aufgabe6.txt")
COUNTS_PER_G = 512  # MMA8452Q with SCALE_4G

# Fenstergröße des Tiefpassfilters
WINDOW_SIZE = 25

# Daten laden
data = np.loadtxt(DATA_FILE)

if data.ndim != 2 or data.shape[1] != 4:
    raise ValueError(
        "Die Messdatei muss vier Spalten enthalten: X, Y, Z und Zeit in ms."
    )

# Zeit in Sekunden
time_seconds = (data[:, 3] - data[0, 3]) / 1000

# Rohdaten in g
acceleration_g = data[:, :3] / COUNTS_PER_G


def moving_average(signal, window):
    kernel = np.ones(window) / window
    return np.convolve(signal, kernel, mode="same")


# Tiefpassfilter auf alle Achsen anwenden
x_filtered = moving_average(acceleration_g[:, 0], WINDOW_SIZE)
y_filtered = moving_average(acceleration_g[:, 1], WINDOW_SIZE)
z_filtered = moving_average(acceleration_g[:, 2], WINDOW_SIZE)

# Plot
plt.figure(figsize=(14, 7))

# Ungefilterte Daten
plt.plot(
    time_seconds,
    acceleration_g[:, 0],
    "--",
    alpha=0.8,
    color="lightblue",
    label="X-Achse ungefiltert"
)

plt.plot(
    time_seconds,
    acceleration_g[:, 1],
    "--",
    alpha=1.0,
    color="moccasin",
    label="Y-Achse ungefiltert"
)

plt.plot(
    time_seconds,
    acceleration_g[:, 2],
    "--",
    alpha=0.8,
    color="lightgreen",
    label="Z-Achse ungefiltert"
)

# Gefilterte Daten
plt.plot(
    time_seconds,
    x_filtered,
    linewidth=2,
    color="tab:blue",
    label="X-Achse gefiltert"
)

plt.plot(
    time_seconds,
    y_filtered,
    linewidth=2,
    color="tab:orange",
    label="Y-Achse gefiltert"
)

plt.plot(
    time_seconds,
    z_filtered,
    linewidth=2,
    color="tab:green",
    label="Z-Achse gefiltert"
)

plt.title("Aufgabe 7 – Vergleich von ungefilterten und gefilterten Beschleunigungsdaten")
plt.xlabel("Zeit [s]")
plt.ylabel("Beschleunigung [g]")
plt.grid(True)
plt.legend(ncol=2)
plt.tight_layout()
plt.show()