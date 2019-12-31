from python_netology.classes.Animals import Cow, Chicken, Duck, Goat, Sheep, Goose

cow = Cow('Манька', 100)
sheep1 = Sheep('Барашек', 20) 
sheep2 = Sheep('Кудрявый', 19)
goat1 = Goat('Рога', 17)
goat2 = Goat('Копыта', 15)
goose1 = Goose('Серый', 5)
goose2 = Goose('Белый', 7)
chicken1 = Chicken('Ко-Ко', 2)
chicken2 = Chicken('Кукареку', 3)
duck = Duck('Кряква', 4)
animals = [cow, sheep1, sheep2, goat1, goat2, goose1, goose2, chicken1, chicken2, duck]
sum_weight = 0
max_weight = 0
name = 0
for animal in animals:
    if animal.weight > max_weight:
        max_weight = animal.weight
        name = animal.name
    sum_weight += animal.weight
print(f"Максимальный вес  {max_weight} у {name}")
print(f'Сумма веса всех животных {sum_weight}')

print(f' Для коровы {cow.name} : {cow.milk()}, {cow.feed()}, {cow.distinguish_by_voice()}')
print(f' Для овцы {sheep1.name} : {sheep1.wool()}, {sheep1.feed()}, {sheep1.distinguish_by_voice()}')
print(f' Для овцы {sheep2.name} : {sheep2.wool()}, {sheep2.feed()}, {sheep2.distinguish_by_voice()}')
print(f' Для козы {goat1.name} : {goat1.milk()}, {goat1.feed()}, {goat1.distinguish_by_voice()}')
print(f' Для козы {goat2.name} : {goat2.milk()}, {goat2.feed()}, {goat2.distinguish_by_voice()}')
print(f' Для гуся {goose1.name} : {goose1.collect_eggs()}, {goose1.feed()}, {goose1.distinguish_by_voice()}')
print(f' Для гуся {goose2.name} : {goose2.collect_eggs()}, {goose2.feed()}, {goose2.distinguish_by_voice()}')
print(f' Для курицы {chicken1.name} : {chicken1.collect_eggs()}, {chicken1.feed()}, {chicken1.distinguish_by_voice()}')
print(f' Для курицы {chicken2.name} : {chicken2.collect_eggs()}, {chicken2.feed()}, {chicken2.distinguish_by_voice()}')
print(f' Для утки {duck.name} : {duck.collect_eggs()}, {duck.feed()}, {duck.distinguish_by_voice()}')
