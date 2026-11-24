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
time_seconds = (
    (timestamps_ms[:-1] + timestamps_ms[1:]) / 2 - timestamps_ms[0]
) / 1000
cumulative_mean_hz = np.cumsum(sampling_frequencies_hz) / np.arange(
    1, len(sampling_frequencies_hz) + 1
)
deviations_hz = sampling_frequencies_hz - mean_frequency_hz

fig, (mean_ax, deviation_ax) = plt.subplots(
    2, 1, figsize=(10, 7), sharex=True
)
mean_ax.plot(
    time_seconds,
    cumulative_mean_hz,
    color="tab:blue",
    label="Laufender Mittelwert",
)
mean_ax.axhline(
    mean_frequency_hz,
    color="tab:orange",
    linestyle="--",
    label=f"Gesamtmittelwert: {mean_frequency_hz:.2f} Hz",
)
mean_ax.set_title("Aufgabe 8 – Abtastfrequenz aus Aufgabe 6")
mean_ax.set_ylabel("Mittelwert [Hz]")
mean_ax.grid(True, alpha=0.4)
mean_ax.legend()

deviation_ax.fill_between(
    time_seconds,
    -std_frequency_hz,
    std_frequency_hz,
    color="tab:orange",
    alpha=0.15,
    label=f"+/- 1 Standardabweichung ({std_frequency_hz:.2f} Hz)",
)
deviation_ax.plot(
    time_seconds,
    deviations_hz,
    color="tab:blue",
    linewidth=0.8,
    label="Abweichung je Messintervall",
)
deviation_ax.axhline(0, color="black", linewidth=1)
deviation_ax.set_xlabel("Zeit [s]")
deviation_ax.set_ylabel("Abweichung [Hz]")
deviation_ax.grid(True, alpha=0.4)
deviation_ax.legend()
fig.tight_layout()
plt.show()
