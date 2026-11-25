# Biosignalverarbeitung

## Ausfuehren

Voraussetzung ist Python 3. Installiere die benoetigten Pakete im Projektordner:

```powershell
python -m pip install -r requirements.txt
python main.py
```

`main.py` fuehrt die Aufgaben 4 bis 9 der Reihe nach aus. Bei Aufgaben mit
Plots das Plotfenster schliessen, damit die naechste Aufgabe startet. Aufgabe 8
gibt Mittelwert und Standardabweichung aus; Aufgabe 9 zeigt die Werte aus
Aufgabe 8 und 9 gemeinsam in einer Tabelle sowie deren Differenz.

## Ordnerstruktur

```text
Bios/
|-- Aufgabe/
|   |-- Aufgabe4/Aufgabe4.py
|   |-- Aufgabe5/Aufgabe5.py
|   |-- Aufgabe6/Aufgabe6.py
|   |-- Aufgabe7/Aufgabe7.py
|   |-- Aufgabe8/Aufgabe8.py
|   `-- Aufgabe9/Aufgabe9.py
|-- data/
|   |-- Aufgabe4.txt
|   |-- Aufgabe5.txt
|   |-- Aufgabe6.txt
|   |-- Aufgabe9_DataLogger.txt
|   `-- Aufgabe9_DataLogger_Alternative.txt
|-- main.py
|-- README.md
|-- requirements.txt
`-- .gitignore
```

Die Messdateien enthalten vier Spalten: X, Y, Z und Zeitstempel in
Millisekunden. Die Skripte laden die Daten aus `data/`, unabhaengig davon, von
welchem Arbeitsverzeichnis aus `main.py` gestartet wird.

Eine neue DataLogger-Aufnahme muss fuer die Auswertung in Aufgabe 9 als
`data/Aufgabe9_DataLogger.txt` abgelegt werden. Die mitgelieferte Datei
`Aufgabe9_DataLogger_Alternative.txt` ist eine weitere Messung und wird nicht
standardmaessig ausgewertet.

