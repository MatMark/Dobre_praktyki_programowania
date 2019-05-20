print("Jadłospis v3")


class Ingredient:

    def __init__(self, name, meaty):
        self.name = name
        self.meaty = meaty


class Meal:

    def __init__(self, name, meaty, ingredients):
        self.name = name
        self.meaty = meaty
        self.ingredients = ingredients


class Menu:

    def __init__(self, ingredients, count):
        self.ingredients = ingredients
        self.count = count


list_of_ingredients = [
    Ingredient("sałata", False),
    Ingredient("grzanki", False),
    Ingredient("kurczak", True),
    Ingredient("pomidory", False),
    Ingredient("ser feta", False),
]

list_of_meals = [
    Meal("sałatka grecka", False, [list_of_ingredients[0], list_of_ingredients[1], list_of_ingredients[3], list_of_ingredients[4]]),
    Meal("sałatka cezar", True, [list_of_ingredients[0], list_of_ingredients[1], list_of_ingredients[2], list_of_ingredients[3]]),
]


def show_names(ls):
    name_list = []
    for x in ls:
        name_list.append(x.name)
    return name_list


def show_meals(ls, meaty):
    name_list = []
    for x in ls:
        if x.meaty == meaty:
            name_list.append(x.name)
    return name_list


def calculate_ingredients(count1, count2, meal1, meal2):
    ing_sum = []

    for x in meal1.ingredients:
        if x in meal2.ingredients:
            ing_sum.append(Menu(x.name, count1 + count2))
        else:
            ing_sum.append(Menu(x.name, count1))

    for x in meal2.ingredients:
        if x not in meal1.ingredients:
            ing_sum.append(Menu(x.name, count2))

    print("Potrzebne składniki: ")
    for x in ing_sum:
        print(str(x.ingredients) + " - " + str(x.count))


def add_new_ingredient():
    print("Dostępne składniki: " + str(show_names(list_of_ingredients)))
    meaty = False
    name = str(input("Podaj nazwę składnika: "))
    ans = str(input("Czy składnik jest mięsny [T/N]?: "))
    while (ans != "T") and (ans != "N"):
        ans = str(input("Czy składnik jest mięsny [T/N]?: "))
    if ans == 'T':
        meaty = True

    ingredient = Ingredient(name, meaty)
    list_of_ingredients.append(ingredient)
    print("Nazwa: " +
          str(ingredient.name) +
          "\nCzy mięsny: " +
          str(ingredient.meaty))


def add_new_meal():
    print("Dostępne dania: " + str(show_names(list_of_meals)))
    name = input("Podaj nazwę dania: ")
    ing = []
    meaty = False

    adding = True
    while adding:
        print("Dostępne składniki: " + str(show_names(list_of_ingredients)))
        tmp = str(input("Podaj nazwę składnika dania: "))

        # szuka czy istnieje taki składnik
        for x in list_of_ingredients:
            if x.name == tmp:
                # jeżeli isnieje to dodaje go do listy składników potrzebnych do tego posiłku
                ing.append(list_of_ingredients[list_of_ingredients.index(x)])
                print("Dodano składnik")
                if x.meaty:
                    meaty = True
                break

        ans = str(input("Dodać kolejny składnik [T/N]?: "))
        while (ans != "T") and (ans != "N"):
            ans = str(input("Dodać kolejny składnik [T/N]?: "))
        if ans == "N":
            adding = False

    meal = Meal(name, meaty, ing)
    list_of_meals.append(meal)
    print("Nazwa: " +
          str(meal.name) +
          "\nCzy mięsny: " +
          str(meal.meaty) +
          "\nLista składników: " +
          str(show_names(meal.ingredients)))
