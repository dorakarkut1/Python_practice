"""
Sposob A:
Rozplaszczamy labirynt rzedami jako wektor (lista) 144 pol.
Ulepszenie:
Usuwamy sciany labiryntu, S, E
Zostawiamy tylko puste pola, ok 70 pol
0 - pole puste
1 - tworzy sciezke

Sposob B:
Chromosomem bedzie ciag ruchow (L, P, G, D) od startu.
L P G D L D
albo liczby
0 1 3 2 1 3 2 0 0
Chromosom jest tym lepszy im bliżej wyjscia sie znajdzie
Odleglosc euklidesowa / manhatan / taksowkowa
Fitness wersja brudna:
    Symulujemy sekwencje gdy zaczynamy od startu
    konczymy gdy dojdziemy do wyjscia lub zatrzymamy sie z braku ruchow
    Zwroc odleglosc konca symulacji od wyjscia
    Zero najlepsza ocena
    Najgorsza -22
    Jak trafi na sciane to bierzemy kolejny ruch

"""

import pygad
import numpy
from itertools import compress
import time

MAT = [[1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,0,1,0,0,0,1,0,0,1], [1,1,1,0,0,0,1,0,1,1,0,1], [1,0,0,0,1,0,1,0,0,0,0,1], [1,0,1,0,1,1,0,0,1,1,0,1], [1,0,0,1,1,0,0,0,1,0,0,1], [1,0,0,0,0,0,1,0,0,0,1,1], [1,0,1,0,0,1,1,0,1,0,0,1], [1,0,1,1,1,0,0,0,1,1,0,1], [1,0,1,0,1,1,0,1,0,1,0,1], [1,0,1,0,0,0,0,0,0,0,0,1], [1,1,1,1,1,1,1,1,1,1,1,1]]
#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0,1,2,3]
gene_dict = {
            0: (0,1),#prawo
            1: (1,0), #dol
            2: (0,-1), #lewo
            3: (-1,0)} #gora
#definiujemy funkcje fitness
def fitness_func(solution, solution_idx):
    start = [1,1]
    kara = 0
    solution_trans = [gene_dict[x] for x in solution]
    for a,b in solution_trans:
        c, d = start[0], start[1]
        if MAT[a + c][b + d] == 0:
            start = [a + c, b + d]
            if start[0] == 10 & start[1] == 10:
                break
    fitness = (10-start[0]) + (10-start[1])
    return -fitness


fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 100
num_genes = 30

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 50
num_generations = 200
keep_parents = 20

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "rank"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 10

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
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["reach_0"])

#uruchomienie algorytmu
start = time.time()
ga_instance.run()
end = time.time()
czas=end-start
#print("Pojedynczy czas: {czas} ".format(czas=czas))
#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
#list_of_things = list(compress(S,solution))
print("Best solution : {solution}".format(solution=solution))
print("Number of generation : {generation}".format(generation=ga_instance.best_solution_generation))
#print("Parameters of the best solution : {solution}".format(solution=list_of_things))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()

tab = []
for e in range(10):
    start = time.time()
    ga_instance.run()
    end = time.time()
    czas = end - start
    tab.append(czas)

print("Sredni czas: {srednia:.2f}".format(srednia=numpy.mean(tab)))

