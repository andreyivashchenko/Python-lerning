purchasedCups = int(input("Введите количество купленных чашек: "))
file = open("bonusCups.txt", 'w')
file.write(f"Количество купленных чашек: {purchasedCups}\n")
file.write(f"Количество бонусных чашек: {purchasedCups // 6}")
file.close()