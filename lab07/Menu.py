from v3 import bib
# from v2 import bib
# from v1 import bib


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
            bib.add_new_ingredient()

        elif usr_type == 2:
            bib.add_new_meal()

        elif usr_type == 3:
            print("Dostępne składniki: " + str(bib.show_names(bib.list_of_ingredients)))

        elif usr_type == 4:
            print("Dostępne dania: " + str(bib.show_names(bib.list_of_meals)))

        elif usr_type == 5:
            meaty_meals = int(input("Podaj liczbę mięsnych posiłków: "))
            vegetarian_meals = int(input("Podaj liczbę wegetariańskich posiłków: "))
            m_meal = ""
            v_meal = ""
            if meaty_meals > 0:
                print(bib.show_meals(bib.list_of_meals, True))
                tmp = str(input("Wybierz posiłki mięsne: "))

                # szuka czy istnieje taki posiłek
                for x in bib.list_of_meals:
                    if (x.name == tmp) and (x.meaty is True):
                        # jeżeli isnieje taki posiłek
                        m_meal = x
                        break

            if vegetarian_meals > 0:
                print(bib.show_meals(bib.list_of_meals, False))
                tmp = str(input("Wybierz posiłki wegetariańskie: "))

                # szuka czy istnieje taki posiłek
                for x in bib.list_of_meals:
                    if (x.name == tmp) and (x.meaty is False):
                        # jeżeli istnieje taki posiłek
                        v_meal = x
                        break
            print("Wybrano " +
                  str(meaty_meals) +
                  " - " +
                  str(m_meal.name) +
                  " i " +
                  str(vegetarian_meals) +
                  " - " +
                  str(v_meal.name)
                  )

            # bib.calculate_ingredients(m_meal, meaty_meals, v_meal, vegetarian_meals)  # v1
            # bib.calculate_ingredients(m_meal, v_meal, meaty_meals, vegetarian_meals)  # v2
            bib.calculate_ingredients(meaty_meals, vegetarian_meals, m_meal, v_meal)  # v3

        elif usr_type == 6:
            end = True

        else:
            print("Nie wybrano poprawnie akcji!")


main()