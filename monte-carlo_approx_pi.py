import random
from math import sqrt, pi
import matplotlib.pyplot as plt

# Définition des paramètres de la simulation
TOTAL_ITERATIONS = 10_000_000
SAMPLE_STEP = 100_000

i_inside = 0  # Points à l'intérieur du cercle
n_list = []      # Liste des totaux d'essais (Axe X)
pi_approx_list = [] # Liste des approximations de pi (Axe Y)

for i_total in range(1, TOTAL_ITERATIONS + 1):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    # Test : le point est-il dans le quart de cercle de rayon 1 ?
    if sqrt(x**2 + y**2) <= 1:
        i_inside += 1

    # Enregistrer l'estimation périodiquement
    if i_total % SAMPLE_STEP == 0:
        # Formule de l'approximation de pi
        pi_approx = (i_inside / i_total) * 4
        n_list.append(i_total)
        pi_approx_list.append(pi_approx)

# --- Tracé du graphique ---
plt.figure(figsize=(12, 7))

# Tracé de l'estimation
plt.plot(n_list, pi_approx_list, label=r'Estimation $\pi$ (Monte Carlo)', color='#1f77b4', linewidth=1)

# Ligne de référence pour la vraie valeur de pi
plt.axhline(pi, color='red', linestyle='--', label=r'Valeur réelle $\pi \approx 3.14159$')

# Formatage
plt.title(f"Approximation de $\pi$ par la méthode de Monte-Carlo (Total : {TOTAL_ITERATIONS:,} essais)", fontsize=16)
plt.xlabel("Nombre total d'essais", fontsize=14)
plt.ylabel(r"Approximation de $\pi$", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.ylim(3.1, 3.25) # Zoom pour montrer la convergence
plt.xlim(0, TOTAL_ITERATIONS)
plt.ticklabel_format(style='plain', axis='x')
plt.tight_layout()

# Sauvegarde du graphique
plt.savefig("pi_monte_carlo_estimation.png")