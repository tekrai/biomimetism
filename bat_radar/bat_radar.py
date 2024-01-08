import numpy as np
import time
import matplotlib.pyplot as plt


# Fonction pour générer un son à haute fréquence
def generate_sound(frequency, duration):
    samples = np.sin(2 * np.pi * frequency * np.arange(duration))
    return samples


# Fonction pour calculer la distance d'un obstacle
def calculate_distance(sound_speed, sound_duration, echo_duration):
    distance = sound_speed * (echo_duration + sound_duration) / 2
    return distance


# Fonction pour calculer la direction d'un obstacle
def calculate_direction(sound_x, sound_y, echo_x, echo_y):
    direction = np.arctan2(echo_y - sound_y, echo_x - sound_x)
    return direction


# Fonction pour générer un schéma représentant le son
def generate_sound_plot(frequency, duration):
    samples = generate_sound(frequency, duration)
    plt.plot(samples)
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    plt.show()
    plt.annotate("Fréquence :", (0, 0.9), size=10)
    plt.annotate(str(frequency), (0.6, 0.9), size=10)
    plt.annotate("Durée :", (0, 0.7), size=10)
    plt.annotate(str(duration), (0.4, 0.7), size=10)


def main():
    # Paramètres de l'algorithme
    frequency = 300  # fréquence du son
    duration = 0.51  # durée du son
    sound_speed = 590  # vitesse du son

    # Initialisation des variables
    robot_x = 3
    robot_y = 2
    obstacle_x = 6
    obstacle_y = 10

    # Émission du son
    print("Émission du son...")
    time.sleep(duration)

    # Calcul de la distance et de la direction de l'obstacle

    distance = calculate_distance(sound_speed, duration, 0.01)
    direction = calculate_direction(robot_x, robot_y, obstacle_x, obstacle_y)
    print('Distance :', distance)
    print('Direction :', f'{direction:.2f}')

    # Affichage du graphique
    generate_sound_plot(frequency, duration)

    # Affichage du graphique de l'obstacle
    plt.plot([obstacle_x, obstacle_x], [obstacle_y, obstacle_y], "o")
    plt.plot([robot_x, obstacle_x], [robot_y, obstacle_y], "-r")
    plt.arrow(obstacle_x, obstacle_y, 0, direction, head_width=0.1, head_length=0.1)
    plt.annotate("Distance :", (obstacle_x + 0.01, obstacle_y + 0.75), size=10)
    plt.annotate(str(distance), (obstacle_x, obstacle_y + 0.25), size=10)
    plt.show()


if __name__ == "__main__":
    main()
