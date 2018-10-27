from data import plants_list

print(plants_list[0])

# for plant in basic_plants_list:
#     print(plant[0])

for plant in plants_list:
    print(plant.name, plant[1])

print()

example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')
example = example._replace(plant_type='whatever')
print(example)
