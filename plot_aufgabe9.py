from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DATA_DIRECTORY = Path(__file__).parent
DATASETS = (
    ("Aufgabe 6", DATA_DIRECTORY / "Aufgabe6.txt"),
    ("Aufgabe 9 (DataLogger)", DATA_DIRECTORY / "ACCdata.txt"),
)


def calculate_sampling_statistics(file_path):
    data = np.loadtxt(file_path)
    if data.ndim != 2 or data.shape[1] != 4:
        raise ValueError(
            f"{file_path.name} muss vier Spalten enthalten: X, Y, Z und Zeit in ms."
        )
    if len(data) < 3:
        raise ValueError(f"{file_path.name} enthält zu wenige Messwerte.")

    timestamps_ms = data[:, 3]
    intervals_ms = np.diff(timestamps_ms)
    if np.any(intervals_ms <= 0):
        raise ValueError(
            f"Die Zeitstempel in {file_path.name} müssen streng ansteigen."
        )

    frequencies_hz = 1000 / intervals_ms
    duration_ms = timestamps_ms[-1] - timestamps_ms[0]
    return {
        "interval_count": len(intervals_ms),
        "duration_seconds": duration_ms / 1000,
        "frequencies_hz": frequencies_hz,
        "mean_hz": np.mean(frequencies_hz),
        "std_hz": np.std(frequencies_hz, ddof=1),
        "overall_hz": len(intervals_ms) * 1000 / duration_ms,
        "mean_interval_ms": np.mean(intervals_ms),
        "std_interval_ms": np.std(intervals_ms, ddof=1),
    }


results = [
    (label, calculate_sampling_statistics(file_path))
    for label, file_path in DATASETS
]

for label, stats in results:
    print(
        f"{label}: {stats['interval_count']} Intervalle, "
        f"{stats['duration_seconds']:.3f} s"
    )
    print(
        f"  Abtastfrequenz: {stats['mean_hz']:.2f} "
        f"+/- {stats['std_hz']:.2f} Hz"
    )
    print(
        f"  Abtastintervall: {stats['mean_interval_ms']:.3f} "
        f"+/- {stats['std_interval_ms']:.3f} ms"
    )
    print(f"  Gesamtrate: {stats['overall_hz']:.2f} Hz")

earlier_mean_hz = results[0][1]["mean_hz"]
logger_mean_hz = results[1][1]["mean_hz"]
difference_hz = logger_mean_hz - earlier_mean_hz
difference_percent = 100 * difference_hz / earlier_mean_hz
print(
    f"Differenz DataLogger zu Aufgabe 6: {difference_hz:+.2f} Hz "
    f"({difference_percent:+.1f} %)"
)

labels = [label for label, _ in results]
means_hz = [stats["mean_hz"] for _, stats in results]
stds_hz = [stats["std_hz"] for _, stats in results]

fig, ax = plt.subplots(figsize=(9, 6))
ax.errorbar(
    labels,
    means_hz,
    yerr=stds_hz,
    fmt="o",
    capsize=8,
    markersize=8,
    color="tab:blue",
    ecolor="tab:orange",
    linewidth=2,
)

for index, (mean_hz, std_hz) in enumerate(zip(means_hz, stds_hz)):
    ax.annotate(
        f"{mean_hz:.2f} +/- {std_hz:.2f} Hz",
        (index, mean_hz),
        xytext=(10, 8),
        textcoords="offset points",
    )

ax.set_title("Aufgabe 9 – Vergleich der Abtastfrequenzen")
ax.set_ylabel("Abtastfrequenz [Hz] (Mittelwert +/- Standardabweichung)")
ax.grid(axis="y", alpha=0.4)
fig.tight_layout()
plt.show()
