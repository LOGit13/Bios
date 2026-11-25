import os
from statistics import mean, stdev


DATA_DIRECTORY = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data")
)
AUFGABE_8_DATEI = os.path.join(DATA_DIRECTORY, "Aufgabe6.txt")
AUFGABE_9_DATEI = os.path.join(DATA_DIRECTORY, "Aufgabe9_DataLogger.txt")


def berechne_abtaststatistik(dateipfad):
    zeitstempel_ms = []
    with open(dateipfad, encoding="utf-8") as datei:
        for zeilennummer, zeile in enumerate(datei, start=1):
            if not zeile.strip():
                continue
            werte = [float(wert) for wert in zeile.split()]
            if len(werte) != 4:
                raise ValueError(
                    f"{dateipfad}, Zeile {zeilennummer}: "
                    "erwartet werden vier Spalten (X, Y, Z, Zeit in ms)."
                )
            zeitstempel_ms.append(werte[3])

    if len(zeitstempel_ms) < 3:
        raise ValueError(f"{dateipfad} enthält zu wenige Messwerte.")

    messintervalle_ms = [
        spaeter - frueher
        for frueher, spaeter in zip(zeitstempel_ms, zeitstempel_ms[1:])
    ]
    if any(intervall <= 0 for intervall in messintervalle_ms):
        raise ValueError(f"Die Zeitstempel in {dateipfad} müssen streng ansteigen.")

    frequenzen_hz = [1000 / intervall for intervall in messintervalle_ms]
    return mean(frequenzen_hz), stdev(frequenzen_hz)


aufgabe_8_mittelwert, aufgabe_8_abweichung = berechne_abtaststatistik(
    AUFGABE_8_DATEI
)
aufgabe_9_mittelwert, aufgabe_9_abweichung = berechne_abtaststatistik(
    AUFGABE_9_DATEI
)

print("Vergleich der Abtastfrequenzen")
print(f"{'Messung':<24} | {'Mittelwert [Hz]':>15} | {'Abweichung [Hz]':>16}")
print("-" * 62)
print(
    f"{'Aufgabe 8':<24} | {aufgabe_8_mittelwert:>15.2f} | "
    f"{aufgabe_8_abweichung:>16.2f}"
)
print(
    f"{'Aufgabe 9 (DataLogger)':<24} | {aufgabe_9_mittelwert:>15.2f} | "
    f"{aufgabe_9_abweichung:>16.2f}"
)

differenz_hz = aufgabe_9_mittelwert - aufgabe_8_mittelwert
differenz_prozent = 100 * differenz_hz / aufgabe_8_mittelwert
print(
    f"\nDifferenz der Mittelwerte (Aufgabe 9 - Aufgabe 8): "
    f"{differenz_hz:+.2f} Hz ({differenz_prozent:+.1f} %)"
)
