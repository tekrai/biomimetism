import random

"""This class creates a new ant with a random path"""


class Ant:
    def __init__(self, n_cities):
        self.path = [0] * n_cities
        self.current_city = 0

    def choose_next_city(self, pheromones):
        """
        This function chooses the next city to visit by the ant. It uses a probability function to choose the city
        with the highest pheromones.
        @rtype: object
        @param pheromones:
        @return:
        """
        possible_cities = list(range(len(pheromones)))
        possible_cities.remove(self.current_city)

        probabilities = [pheromones[self.current_city][i] / sum(pheromones[self.current_city]) for i in possible_cities]
        next_city = random.choices(possible_cities, weights=probabilities)[0]

        return next_city

    def add_pheromone(self, pheromones):
        """
        This function adds a pheromone to the path segment traveled by the ant.
        @rtype: object
        @param pheromones:
        """
        pheromones[self.current_city][self.path[self.current_city]] += 1


"""This class creates a new ant system with the specified parameters."""


class AntSystem:
    def __init__(self, n_cities, pheromones_init):
        self.n_cities = n_cities
        self.pheromones = pheromones_init
        self.ants = [Ant(n_cities) for _ in range(n_cities)]

    def evaluate_solution(self):
        """
        This function evaluates the current solution of the ant system. It returns the length of the shortest path found.
        @rtype: object
        @return:
        """
        lengths_of_paths = []
        for ant in self.ants:
            lengths_of_paths.append(ant.path)

        return min(lengths_of_paths)

    def iterate(self):
        """
        This function performs one iteration of the ant system algorithm. It makes the ants walk on the graph and deposit pheromones.
        @rtype: object
        """
        for ant in self.ants:
            for i in range(self.n_cities - 1):
                next_city = ant.choose_next_city(self.pheromones)
                ant.path[i + 1] = next_city
                ant.current_city = next_city

        for ant in self.ants:
            ant.add_pheromone(self.pheromones)

    def run(self, max_iters):
        """
        This function runs the ant system algorithm for a specified number of iterations. It returns the length of the shortest path found.
        @rtype: object
        @param max_iters:
        @return: the solution evaluate
        """
        for _ in range(max_iters):
            self.iterate()

        return self.evaluate_solution()


if __name__ == "__main__":
    # Initialize parameters
    n_cities = 10
    pheromones_init = [[1] * n_cities for _ in range(n_cities)]

    # Create ant system
    ant_system = AntSystem(n_cities, pheromones_init)

    # Run the algorithm
    solution = ant_system.run(1000)

    # Print the solution
    print(solution)
