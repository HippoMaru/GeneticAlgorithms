import random

# GA params
POPULATION_SIZE = 30
LAND_SIZE = 10
CROSSOVER_PROBABILITY = 0.9
MUTATION_PROBABILITY = 0.005
MAX_GENERATIONS = 1000

RANDOM_SEED = 1488
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
        return fitness


# GA
def create_coloring(vertexes_number, colors_number):
    return Coloring([random.randint(0, colors_number - 1) for i in range(vertexes_number)])


def create_population(vertexes_number, colors_number):
    return [create_coloring(vertexes_number, colors_number) for i in range(POPULATION_SIZE)]


def get_best_coloring(population, edges_list) -> Coloring:
    best_fitness = 0
    best_coloring = population[0]
    for c in population:
        if c.calculate_fitness(edges_list) > best_fitness:
            best_fitness = c.calculate_fitness(edges_list)
            best_coloring = c
    return best_coloring


def selection(population, edges_list):
    tournament_result = []
    best_coloring = get_best_coloring(population, edges_list)
    tournament_population = []
    for i in range(POPULATION_SIZE):
        if population[i] != best_coloring:
            tournament_population.append(Coloring(population[i].copy()))
        else:
            for j in range(i + 1, POPULATION_SIZE):
                tournament_population.append(Coloring(population[j].copy()))
            break
    for i in range(POPULATION_SIZE - 1):
        c1 = c2 = c3 = 0
        while c1 == c2 or c1 == c3 or c2 == c3:
            c1, c2, c3 = random.randint(0, POPULATION_SIZE-2),\
                         random.randint(0, POPULATION_SIZE-2),\
                         random.randint(0, POPULATION_SIZE-2)

        tournament_result.append(get_best_coloring([tournament_population[c1],
                                                    tournament_population[c2],
                                                    tournament_population[c3]], edges_list))
    tournament_result.append(best_coloring)
    return tournament_result


def breed(parent_1, parent_2):
    size = len(parent_1)
    cross_point = random.randint(0, size - 1)
    child_1 = Coloring(parent_1[0:cross_point] + parent_2[cross_point:])
    child_2 = Coloring(parent_2[0:cross_point] + parent_1[cross_point:])
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


def mutation(population, colors_number):
    for coloring in population:
        if random.randrange(0, 1) <= MUTATION_PROBABILITY:
            size = len(coloring)
            mutated_gen = random.randint(0, size - 1)
            coloring[mutated_gen] = random.randint(0, colors_number - 1)
    return population


def check_generation(population, edges_list):
    for coloring in population:
        if coloring.calculate_fitness(edges_list) == len(edges_list):
            return True
    return False


def GA(vertexes_list, adjacency_matrix):
    n = len(vertexes_list)
    edges_list = []
    for i in range(n):
        for j in range(i+1, n):
            if adjacency_matrix[i][j] == 1:
                edges_list.append([i, j])
    g1 = Graph(n, edges_list)
    colors_number = g1.vertexes_number
    result_number = colors_number + 1
    result_coloring = [i for i in range(g1.vertexes_number)]

    while colors_number >= 1:
        # print(result_number, '\t\t', result_coloring)
        break_key = True
        population = create_population(g1.vertexes_number, colors_number)
        for coloring in population:
            coloring.calculate_fitness(g1.edges_list)
        g_counter = 0
        while g_counter <= MAX_GENERATIONS:
            population = selection(population, g1.edges_list)
            population = crossover(population)
            population = mutation(population, colors_number)
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
    result_dict = {}
    for i in range(n):
        result_dict[vertexes_list[i]] = result_coloring[i]
    return result_dict
    # print(result_number, '\t\t', result_coloring)

def GA_evolution(vertexes_list, adjacency_matrix, step):
    result = []
    n = len(vertexes_list)
    edges_list = []
    for i in range(n):
        for j in range(i+1, n):
            if adjacency_matrix[i][j] == 1:
                edges_list.append([i, j])
    # g1 = Graph()
    g1 = Graph(n, edges_list)
    colors_number = g1.vertexes_number
    result_number = colors_number + 1
    result_coloring = [i for i in range(g1.vertexes_number)]

    while colors_number >= 1:
        this_color_result = [colors_number, []]
        # print(result_number, '\t\t', result_coloring)
        break_key = True
        population = create_population(g1.vertexes_number, colors_number)
        for coloring in population:
            coloring.calculate_fitness(g1.edges_list)
        g_counter = 0
        while g_counter <= MAX_GENERATIONS:
            population = selection(population, g1.edges_list)
            population = crossover(population)
            population = mutation(population, colors_number)
            if check_generation(population, g1.edges_list):
                result_number = colors_number
                result_coloring = get_best_coloring(population, g1.edges_list)
                result_dict = {}
                for i in range(n):
                    result_dict[vertexes_list[i]] = result_coloring[i]
                this_color_result[1].append(result_dict)
                result.append(this_color_result)
                colors_number -= 1
                break_key = False
                break
            else:
                if g_counter % step == 0:
                    best_coloring = get_best_coloring(population, g1.edges_list)
                    result_dict = {}
                    for i in range(n):
                        result_dict[vertexes_list[i]] = best_coloring[i]
                    this_color_result[1].append(result_dict)
                g_counter += 1
        if break_key:
            break
    return result
    # print(result_number, '\t\t', result_coloring)


# print(GA([2, 4, 8, 6], [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]))
