from selenium import webdriver
import unittest


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
    
    def test_app_dynamics_job(self):
        global EUR, GBP, USD, old_EUR, old_GBP, old_USD
        driver = self.driver
        driver.get("https://www.nbp.pl/home.aspx?f=/kursy/kursya.html")
        EUR = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='euro'])[1]/following::td[2]").text
        GBP = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='funt szterling'])[1]/following::td[2]").text
        USD = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='dolar amerykański'])[1]/following::td[2]").text
        EUR = EUR.replace(",", ".")
        GBP = GBP.replace(",", ".")
        USD = USD.replace(",", ".")

        file = open("savedData.txt", "r")
        old_EUR = (file.readline())
        old_GBP = (file.readline())
        old_USD = (file.readline())
        file.close()

        self.assertEqual(float(old_EUR), float(EUR))
        self.assertEqual(float(old_GBP), float(GBP))
        self.assertEqual(float(old_USD), float(USD))
    
    def tearDown(self):
        global EUR, GBP, USD, old_EUR, old_GBP, old_USD

        if float(EUR) == float(old_EUR):
            print("Euro: " + EUR + " bez zmian")
        elif float(EUR) < float(old_EUR):
            print("Euro: " + EUR + " spadek z " + old_EUR)
        else:
            print("Euro: " + EUR + " wzrost z " + old_EUR)

        if float(GBP) == float(old_GBP):
            print("Funt: " + GBP + " bez zmian")
        elif float(GBP) < float(old_GBP):
            print("Funt: " + GBP + " spadek z " + old_GBP)
        else:
            print("Funt: " + GBP + " wzrost z " + old_GBP)

        if float(USD) == float(old_USD):
            print("Dolar: " + USD + " bez zmian")
        elif float(USD) < float(old_USD):
            print("Dolar: " + USD + " spadek z " + old_USD)
        else:
            print("Dolar: " + USD + " wzrost z " + old_USD)
        f = open("savedData.txt", "w+")
        f.write(str(EUR) + "\n" + str(GBP) + "\n" + str(USD))
        f.close()

        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
