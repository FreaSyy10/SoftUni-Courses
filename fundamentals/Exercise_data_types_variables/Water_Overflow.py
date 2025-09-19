number_lines=int(input())
tank_capacity =255

for curremt_line in range(number_lines):
    litres_of_water=int(input())

    if tank_capacity <litres_of_water:
        print("Insufficient capacity!")
        continue

    tank_capacity -= litres_of_water
print(255-tank_capacity)