maxCount = 0
totalCount = 0
maxAnimals = None

enterFile = open('farm.txt', 'r', encoding='utf8')

for el in enterFile:
    animal, count = el.split(' ')
    match animal:
        case 'курицы' | "утки":
            totalCount += int(count) * 2
        case _:
            totalCount += int(count) * 4
    if int(count) >= maxCount:
        maxAnimals = animal
        maxCount = int(count)

enterFile.close()

outFile = open('Out.txt', 'w')
outFile.write(f"На ферме больше всего: {maxAnimals}")
outFile.close()

print(f"Общее количество ног: {totalCount}")
