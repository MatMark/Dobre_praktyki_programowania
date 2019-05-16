print("Jadłospis v1")


class Ingredient:

    def __init__(self, name, meaty):
        self.name = name
        self.meaty = meaty


class Meal:

    def __init__(self, name, meaty, ingredients):
        self.name = name
        self.meaty = meaty
        self.ingredients = ingredients


list_of_ingredients = [
    Ingredient("jaja", False),
    Ingredient("chleb", False),
    Ingredient("wieprzowina", True),
]

list_of_meals = [
    Meal("jajecznica", False, [list_of_ingredients[0], list_of_ingredients[1]]),
    Meal("jajecznica na boczku", True, [list_of_ingredients[0], list_of_ingredients[1], list_of_ingredients[2]]),
]


def show_names(ing_list):
    name_list = []
    for x in ing_list:
        name_list.append(x.name)
    return name_list


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


def main():
    end = False
    while not end:

        usr_type = int(input("\nCo chcesz zrobić:\n"
                             "1-Dodać składnik\n"
                             "2-Dodać danie\n"
                             "3-Wyświetlić składniki\n"
                             "4-Wyświetlić dania\n"
                             "5-Stworzyć jadłospis\n"
                             "6-Wyjść z aplikacji\n"
                             ))

        if usr_type == 1:
            add_new_ingredient()

        elif usr_type == 2:
            add_new_meal()

        elif usr_type == 3:
            print("Dostępne składniki: " + str(show_names(list_of_ingredients)))

        elif usr_type == 4:
            print("Dostępne dania: " + str(show_names(list_of_meals)))

        elif usr_type == 5:
            print("Work in progress")
            # meaty_meals = int(input("Podaj liczbę mięsnych posiłków: "))
            # vegetarian_meals = int(input("Podaj liczbę wegetariańskich posiłków: "))

        elif usr_type == 6:
            end = True

        else:
            print("Nie wybrano poprawnie akcji!")


main()
