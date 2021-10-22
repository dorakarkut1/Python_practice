#cwiczenia 1

import numpy as np

#Zad 1
a = 123
b = 321
print(a+b)
print("-------------------------------")
#wektorki
a = np.array([3, 8, 9, 10, 12])
b = np.array([8, 7, 7, 5, 6])
print(a+b)
print(a*b)
print(np.dot(a,b))
print("Dystans euklidesowy 1: ", np.linalg.norm(a))
print("Dystans euklidesowy 2: ", np.linalg.norm(b))
print("-------------------------------")
#macierze

macierz1 = np.random.randint(0,100,np.array((3,3)))
macierz2 = np.random.randint(0,100,np.array((3,3)))

print(macierz1)
print(macierz2)
print(macierz1*macierz2)
print(np.dot(macierz1,macierz2))

print("-------------------------------")

wektor = np.random.randint(0,100, np.array([50]))
print(wektor)
srednia = wektor.mean()
print(srednia)
minimum = wektor.min()
print("indeks najmniejszego elem: ", list(wektor).index(minimum))
print(minimum)
maximum = wektor.max()
print("indeks najwiekszego elem: ", list(wektor).index(maximum))
print(maximum)
odchylenie = wektor.std()
print(odchylenie)
print("-------------------------------")
wektor_std = np.array([50])
wektor_std = [((x-minimum)/(maximum-minimum)) for x in wektor]
wektor_std = np.array(wektor_std)
print(wektor_std)
srednia = wektor_std.mean()
print(srednia)
minimum = wektor_std.min()
print("indeks najmniejszego elem: ", list(wektor_std).index(minimum))
print(minimum)
maximum = wektor_std.max()
print("indeks najwiekszego elem: ", list(wektor_std).index(maximum))
print(maximum)
odchylenie = wektor_std.std()
print(odchylenie)