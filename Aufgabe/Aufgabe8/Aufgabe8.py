import os
from statistics import mean, stdev


DATA_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "Aufgabe6.txt")
)

with open(DATA_FILE, encoding="utf-8") as data_file:
    data = [
        [float(value) for value in line.split()]
        for line in data_file
        if line.strip()
    ]

if any(len(row) != 4 for row in data):
    raise ValueError("Die Messdatei muss vier Spalten enthalten: X, Y, Z und Zeit in ms.")
if len(data) < 3:
    raise ValueError(
        "Für die Frequenzbestimmung werden mindestens drei Messwerte benötigt."
    )

# Die Zeitstempel stehen in Millisekunden; jeder Abstand ergibt ein Intervall.
timestamps_ms = [row[3] for row in data]
sample_intervals_ms = [
    later - earlier
    for earlier, later in zip(timestamps_ms, timestamps_ms[1:])
]
if any(interval <= 0 for interval in sample_intervals_ms):
    raise ValueError("Die Zeitstempel müssen streng monoton ansteigen.")

mean_interval_ms = mean(sample_intervals_ms)
std_interval_ms = stdev(sample_intervals_ms)

sampling_frequencies_hz = [1000 / interval for interval in sample_intervals_ms]
mean_frequency_hz = mean(sampling_frequencies_hz)
std_frequency_hz = stdev(sampling_frequencies_hz)

print("Aufgabe 8: Zeitintervall und Abtastfrequenz")
print(f"{'Messgroesse':<26}{'Mittelwert':>15}{'Standardabweichung':>25}")
print(
    f"{'Zeitintervall [ms]':<26}"
    f"{mean_interval_ms:>12.3f} ms"
    f"{std_interval_ms:>20.3f} ms"
)
print(
    f"{'Abtastfrequenz [Hz]':<26}"
    f"{mean_frequency_hz:>12.3f} Hz"
    f"{std_frequency_hz:>20.3f} Hz"
)
