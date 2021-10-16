import pygad
import numpy
from itertools import compress

S = [(100,7), (300,7), (200,6), (40,2), (500,5), (70,6), (100,1), (250,3), (300,10), (280,3), (300,15)]
ALL_VAL = numpy.sum([x for (x,y) in S])
WEIGHT = 25
#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcjÄ fitness
def fitness_func(solution, solution_idx):
    list_of_things = list(compress(S,solution))
    sum_val = numpy.sum([x for (x,y) in list_of_things])
    sum_weight = numpy.sum([y for (x, y) in list_of_things])
    if sum_weight <= WEIGHT:
        fitness = -1/(1+sum_val)
        return fitness
    else:
        return -2

fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 50
num_genes = len(S)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 25
num_generations = 100
keep_parents = 3

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "rank"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 20

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

#uruchomienie algorytmu
ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
list_of_things = list(compress(S,solution))
sum_val = numpy.sum([x for (x,y) in list_of_things])
print("Wartosc: ", sum_val)
sum_weight = numpy.sum([y for (x, y) in list_of_things])
print("Waga: ",sum_weight)


#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()