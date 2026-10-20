import pandas as pd
import matplotlib.pyplot as plt

before = pd.DataFrame({
    "users": [5, 10, 20],
    "avg_time": [254.46, 138.11, 181.63]
})

after = pd.DataFrame({
    "users": [5, 10, 20],
    "avg_time": [26.5, 33.79, 62.06]
})

plt.figure(figsize=(8,5))

plt.plot(
    before["users"],
    before["avg_time"],
    marker="o",
    label="Antes optimización"
)

plt.plot(
    after["users"],
    after["avg_time"],
    marker="o",
    label="Después optimización"
)

plt.title("Comparación de rendimiento")
plt.xlabel("Usuarios concurrentes")
plt.ylabel("Tiempo medio (s)")
plt.legend()
plt.grid(True)

plt.savefig("performance_comparison.png")

print("Gráfica guardada en performance_comparison.png")
