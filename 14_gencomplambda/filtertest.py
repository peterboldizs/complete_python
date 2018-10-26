food = ["apple", "maple", "egg", "pork", "beef"]


def no_egg(food_list: list):
    return "egg" not in food_list


eggless = list(filter(no_egg, food))
print(eggless)
