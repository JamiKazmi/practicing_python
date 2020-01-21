numbers = [1, 2, 3, 4, 4, 3, 0, 10, 11, 10]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

uniques.sort()
print(uniques)
