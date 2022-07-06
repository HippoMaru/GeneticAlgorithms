import random

# GA params
POPULATION_SIZE = 30
LAND_SIZE = 10
CROSSOVER_PROBABILITY = 0.9
MUTATION_PROBABILITY = 0.005
MAX_GENERATIONS = 1000

RANDOM_SEED = 10
random.seed(RANDOM_SEED)


# Sup things
class Graph:
    def __init__(self, vertexes_number=10, edges_list=None):
        if edges_list is None:
            edges_list = [[0, 1], [1, 2], [1, 3], [1, 5], [3, 6], [3, 7], [4, 8], [4, 9], [6, 7], [6, 9]]
        self.edges_list = edges_list
        self.vertexes_number = vertexes_number


class Coloring(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = 0

    def calculate_fitness(self, edges_list):
        fitness = len(edges_list)
        for edge in edges_list:
            if self[edge[0]] == self[edge[1]]:
                fitness -= 1
        self.fitness = fitness


# GA
def create_coloring(vertexes_number, colors_number):
    return Coloring([random.randint(0, colors_number - 1) for i in range(vertexes_number)])


def create_population(vertexes_number, colors_number):
    return [create_coloring(vertexes_number, colors_number) for i in range(POPULATION_SIZE)]


def coloring_sorting(coloring):
    return coloring.fitness


def selection(population, edges_list):
    tournament_result = []
    tournament = [[], [], []]
    best_coloring = get_best_coloring(population)
    i = 0
    for coloring in population:
        if coloring != best_coloring:
            tournament[i].append(coloring)
            i += 1
            i %= 3
    for group in tournament:
        tournament_result.append(get_best_coloring(group))
    tournament_result.append(best_coloring)
    generation = population.copy()
    for coloring in tournament_result:
        if coloring not in generation:
            generation.append(coloring)
    result = generation.sort(key=coloring_sorting)[LAND_SIZE]
    return result


def breed(parent_1, parent_2):
    size = len(parent_1)
    cross_point = random.randint(0, size - 1)
    child_1 = parent_1[0:cross_point] + parent_2[cross_point:]
    child_2 = parent_2[0:cross_point] + parent_1[cross_point:]
    return child_1, child_2


def crossover(population):
    for i in range(len(population)//2):
        if random.randrange(0, 1) <= CROSSOVER_PROBABILITY:
            parent_1 = population[2*i]
            parent_2 = population[2*i + 1]
            child_1, child_2 = breed(parent_1, parent_2)
            population[2*i] = child_1
            population[2*i + 1] = child_2
    return population


def mutation(population):
    for coloring in population:
        if random.randrange(0, 1) <= MUTATION_PROBABILITY:
            size = len(coloring)
            mutated_gen = random.randint(0, size - 1)
            coloring[mutated_gen] = random.randint(0, colors_number - 1)
    return population


def check_generation(population, edges_list):
    for coloring in population:
        if coloring.calculate_fitness() == len(edges_list):
            return True
    return False


def get_best_coloring(population, edges_list) -> Coloring:
    best_fitness = 0
    best_coloring = population[0]
    for coloring in population:
        if coloring.calculate_fitness(edges_list) > best_fitness:
            best_fitness = coloring.calculate_fitness(edges_list)
            best_coloring = coloring
    return best_coloring


g1 = Graph()
colors_number = g1.vertexes_number
result_number = colors_number + 1
result_coloring = [i for i in range(g1.vertexes_number)]

while colors_number >= 1:
    break_key = True
    population = create_population(g1.vertexes_number, colors_number)
    for coloring in population:
        coloring.calculate_fitness(g1.edges_list)
    fitness_values = [coloring.fitness for coloring in population]
    g_counter = 0
    while g_counter <= MAX_GENERATIONS:
        population = selection(population, g1.edges_list)
        population = crossover(population)
        population = mutation(population)
        if check_generation(population, g1.edges_list):
            result_number = colors_number
            result_coloring = get_best_coloring(population, g1.edges_list)
            colors_number -= 1
            break_key = False
            break
        else:
            g_counter += 1
    if break_key:
        break

print(result_number, '\t\t', result_coloring)
