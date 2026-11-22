import matplotlib.pyplot as plt

# Rohdaten des MMA8452Q bei SCALE_2G (1024 Counts pro g)
x_counts = [-81, 172, 233, 95, 192, 297]
y_counts = [2047, 2047, 2047, 2047, 2047, 2047]
z_counts = [677, 406, 494, 638, 278, 532]
counts_per_g = 1024

x = [wert / counts_per_g for wert in x_counts]
y = [wert / counts_per_g for wert in y_counts]
z = [wert / counts_per_g for wert in z_counts]

# Zeit in ms
t = [5699, 6331, 6962, 7592, 8224, 8855]

# Zeit auf Sekunden normieren
t = [(wert - t[0]) / 1000 for wert in t]

# Plot
plt.figure(figsize=(10,5))

plt.plot(t, x, marker='o', label='X-Achse')
plt.plot(t, y, marker='o', label='Y-Achse')
plt.plot(t, z, marker='o', label='Z-Achse')

plt.title('Beschleunigungssensor - 4 Sekunden Messung')
plt.xlabel('Zeit [s]')
plt.ylabel('Beschleunigung [g]')
plt.legend()
plt.grid(True)

plt.show()