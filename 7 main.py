from itertools import permutations

cities = ["Москва", "Владикавказ", "Челябинск", "Новосибирск"]
start = "Москва"
end = "Новосибирск"

count = 0
for perm in permutations(cities):
    if perm[0] == start and perm[-1] == end:
        count += 1

print(count)