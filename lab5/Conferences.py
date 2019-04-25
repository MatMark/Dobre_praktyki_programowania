import random


class Conference:
    def __init__(self, title, author, date, description):
        self.title = title
        self.author = author
        self.sections = []
        self.date = date
        self.description = description
        self.participants = []


conferenceList = []
active_user = ""


def pay():
    price = random.randint(100, 350)
    ans = str(input("Czy chcesz zapłacić " + str(price) +
                    "zł za udział w konferencji?: [T/N]"))
    while (ans != "T") and (ans != "N"):
        ans = str(input("Czy chcesz zapłacić " + str(price) +
                        "zł za udział w konferencji?: [T/N]"))
    if ans == "T":
        return True
    else:
        return False


def login():
    global active_user
    active_user = str(input("Podaj nazwę użytkownika: "))


def show_conference_list():
    for conference in conferenceList:
        print("Tytuł: " + conference.title +
              "\nAutor: " + conference.author +
              "\nSekcje: " + str(conference.sections) +
              "\nData: " + conference.date +
              "\nOpis: " + conference.description +
              "\nUczestnicy: " + str(conference.participants) +
              "\n\n")


def admin():
    global conferenceList, active_user
    print("Wybrano admina")
    login()
    end = False
    while not end:
        case = int(input("Wybierz działanie:\n"
                         "1-Dodaj nową konferencję\n"
                         "2-Wyświetl listę konferencji\n"
                         "3-Wyloguj\n"))

        if case == 1:
            title = str(input("Tytuł konfrencji: "))
            date = str(input("Data konferencji: "))
            description = str(input("Opis konferencji: "))
            tmp_conf = Conference(title, active_user, date, description)

            adding = True
            while adding:
                tmp_conf.sections.append(str(input("Nazwa sekcji: ")))
                ans = str(input("Dodać kolejną [T/N]?: "))
                while (ans != "T") and (ans != "N"):
                    ans = str(input("Dodać kolejną [T/N]?: "))
                if ans == "N":
                    adding = False

            conferenceList.append(tmp_conf)

        elif case == 2:
            show_conference_list()

        elif case == 3:
            end = True

        else:
            print("Nie wybrano poprawnego działania")


def speaker():
    global conferenceList, active_user
    print("Wybrano prelegenta")
    login()
    end = False
    abstrakt = False
    while not end:

        case = int(input("Wybierz działanie:\n"
                         "1-Zapisz się na konferencję\n"
                         "2-Wyświetl listę konferencji\n"
                         "3-Dodaj abstrakt\n"
                         "4-Wyloguj\n"))

        if case == 1:
            if abstrakt:
                conf_title = str(input("Nazwa konferencji, na którą chcesz się zapisać: "))

                for conference in conferenceList:
                    if conference.title == conf_title:
                        if pay():
                            conference.participants.append(active_user)
                            print("Zapisano na konferencję o nazwie " + conf_title)
                        else:
                            print("Nie opłacono konferencji")
                        return
                    else:
                        print("Nie ma konferencji o podanej nazwie")
            else:
                print("Dodaj najpierw abstrakt")

        elif case == 2:
            show_conference_list()

        elif case == 3:
            abstrakt = True
            print("Poprawnie dodano abstrakt")

        elif case == 4:
            end = True

        else:
            print("Nie wybrano poprawnego działania")


def participant():
    global conferenceList, active_user
    print("Wybrano uczestnika")
    login()
    end = False
    while not end:

        case = int(input("Wybierz działanie:\n"
                         "1-Zapisz się na konferencję\n"
                         "2-Wyświetl listę konferencji\n"
                         "3-Wyloguj\n"))

        if case == 1:
            conf_title = str(input("Nazwa konferencji, którą chcsz się zapisać: "))

            for conference in conferenceList:
                if conference.title == conf_title:
                    if pay():
                        conference.participants.append(active_user)
                        print("Zapisano na konferencję o nazwie " + conf_title)
                    else:
                        print("Nie opłacono konferencji")
                    return
                else:
                    print("Nie ma konferencji o podanej nazwie")

        elif case == 2:
            show_conference_list()

        elif case == 3:
            end = True

        else:
            print("Nie wybrano poprawnego działania")


def main():
    end = False
    while not end:

        usr_type = int(input("Wybierz typ użytkownika:\n"
                             "1-Admin\n"
                             "2-Prelegent\n"
                             "3-Uczestnik\n"
                             "4-Wyjdź z aplikacji\n"))

        if usr_type == 1:
            admin()

        elif usr_type == 2:
            speaker()

        elif usr_type == 3:
            participant()

        elif usr_type == 4:
            end = True

        else:
            print("Nie wybrano poprawnie typu użytkownika!")


main()
