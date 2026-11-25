import os

import matplotlib.pyplot as plt
import numpy as np

datei_pfad = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "Aufgabe6.txt")
)
zaehlwerte_pro_g = 512

# Fenstergröße des Tiefpassfilters
fenstergroesse = 25

# Daten laden
messdaten = np.loadtxt(datei_pfad)

if messdaten.ndim != 2 or messdaten.shape[1] != 4:
    raise ValueError(
        "Die Messdatei muss vier Spalten enthalten: X, Y, Z und Zeit in ms."
    )

# Zeit in Sekunden
zeit_sekunden = (messdaten[:, 3] - messdaten[0, 3]) / 1000

# Rohdaten in g
beschleunigung_g = messdaten[:, :3] / zaehlwerte_pro_g


def gleitender_mittelwert(messreihe, fenstergroesse):
    mittelungsfenster = np.ones(fenstergroesse) / fenstergroesse
    return np.convolve(messreihe, mittelungsfenster, mode="same")


# Tiefpassfilter auf alle Achsen anwenden
x_gefiltert = gleitender_mittelwert(beschleunigung_g[:, 0], fenstergroesse)
y_gefiltert = gleitender_mittelwert(beschleunigung_g[:, 1], fenstergroesse)
z_gefiltert = gleitender_mittelwert(beschleunigung_g[:, 2], fenstergroesse)

# Plot
plt.figure(figsize=(14, 7))

# Ungefilterte Daten
plt.plot(
    zeit_sekunden,
    beschleunigung_g[:, 0],
    "--",
    alpha=0.8,
    color="lightblue",
    label="X-Achse ungefiltert"
)

plt.plot(
    zeit_sekunden,
    beschleunigung_g[:, 1],
    "--",
    alpha=1.0,
    color="moccasin",
    label="Y-Achse ungefiltert"
)

plt.plot(
    zeit_sekunden,
    beschleunigung_g[:, 2],
    "--",
    alpha=0.8,
    color="lightgreen",
    label="Z-Achse ungefiltert"
)

# Gefilterte Daten
plt.plot(
    zeit_sekunden,
    x_gefiltert,
    linewidth=2,
    color="tab:blue",
    label="X-Achse gefiltert"
)

plt.plot(
    zeit_sekunden,
    y_gefiltert,
    linewidth=2,
    color="tab:orange",
    label="Y-Achse gefiltert"
)

plt.plot(
    zeit_sekunden,
    z_gefiltert,
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