from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DATA_FILE = Path(__file__).with_name("Aufgabe6.txt")

data = np.loadtxt(DATA_FILE)
if data.ndim != 2 or data.shape[1] != 4:
    raise ValueError(
        "Die Messdatei muss vier Spalten enthalten: X, Y, Z und Zeit in ms."
    )
if len(data) < 3:
    raise ValueError(
        "Für die Frequenzbestimmung werden mindestens drei Messwerte benötigt."
    )

timestamps_ms = data[:, 3]
sample_intervals_ms = np.diff(timestamps_ms)
if np.any(sample_intervals_ms <= 0):
    raise ValueError("Die Zeitstempel müssen streng monoton ansteigen.")

sampling_frequencies_hz = 1000 / sample_intervals_ms
mean_frequency_hz = np.mean(sampling_frequencies_hz)
std_frequency_hz = np.std(sampling_frequencies_hz, ddof=1)
overall_frequency_hz = (
    len(sample_intervals_ms) * 1000 / (timestamps_ms[-1] - timestamps_ms[0])
)

time_seconds = (timestamps_ms - timestamps_ms[0]) / 1000
interval_midpoints_seconds = (time_seconds[:-1] + time_seconds[1:]) / 2

print(f"Ausgewertete Abtastintervalle: {len(sample_intervals_ms)}")
print(
    f"Abtastfrequenz: {mean_frequency_hz:.2f} "
    f"+/- {std_frequency_hz:.2f} Hz"
)
print(
    f"Abtastintervall: {np.mean(sample_intervals_ms):.3f} "
    f"+/- {np.std(sample_intervals_ms, ddof=1):.3f} ms"
)
print(f"Gesamt-Abtastrate über die Messdauer: {overall_frequency_hz:.2f} Hz")

plt.figure(figsize=(14, 6))
plt.axhspan(
    mean_frequency_hz - std_frequency_hz,
    mean_frequency_hz + std_frequency_hz,
    color="tab:red",
    alpha=0.15,
    label="Mittelwert +/- 1 Standardabweichung",
)
plt.plot(
    interval_midpoints_seconds,
    sampling_frequencies_hz,
    ".",
    color="tab:blue",
    alpha=0.5,
    markersize=3,
    label="Frequenz je Abtastintervall",
)
plt.axhline(
    mean_frequency_hz,
    color="tab:red",
    linewidth=2,
    label=f"Mittelwert: {mean_frequency_hz:.2f} Hz",
)
plt.title(
    "Aufgabe 8 – Abtastfrequenz: "
    f"{mean_frequency_hz:.2f} +/- {std_frequency_hz:.2f} Hz"
)
plt.xlabel("Zeit [s]")
plt.ylabel("Abtastfrequenz [Hz]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
