import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda senoidal original
frecuencia = 1.0  # Frecuencia en Hz
amplitud = 1.0    # Amplitud de la onda
fase = 0          # Fase inicial en radianes
duracion = 2.0    # Duración de la señal en segundos
fs_original = 100 # Frecuencia de muestreo para la onda original

# Generar la onda senoidal original
t_original = np.linspace(0, duracion, int(fs_original * duracion), endpoint=False)
onda_original = amplitud * np.sin(2 * np.pi * frecuencia * t_original + fase)

# Aproximación de Euler para diferentes pasos de muestreo
def euler_approx(dt):
    t_euler = np.arange(0, duracion, dt)
    onda_euler = np.zeros_like(t_euler)
    y = 0  # Valor inicial
    for i in range(1, len(t_euler)):
        y += amplitud * 2 * np.pi * frecuencia * np.cos(2 * np.pi * frecuencia * t_euler[i-1] + fase) * dt
        onda_euler[i] = y
    return t_euler, onda_euler

# Parámetros de los pasos de muestreo
dt_values = [0.1, 0.05, 0.02]

# Crear subplots
fig, axs = plt.subplots(3, 1, figsize=(12, 12))

for i, dt in enumerate(dt_values):
    t_euler, onda_euler = euler_approx(dt)
    axs[i].plot(t_original, onda_original, label='Onda Senoidal Original', linewidth=2)
    axs[i].plot(t_euler, onda_euler, 'o-', label=f'Aproximación de Euler (dt={dt})', markersize=4)
    axs[i].set_xlabel('Tiempo [s]')
    axs[i].set_ylabel('Amplitud')
    axs[i].legend()
    axs[i].grid()
    axs[i].set_title(f'Comparación para dt={dt}')

plt.tight_layout()
plt.show()
