import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class ProjektTest(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne:
        # 1. Otwarta strona główna
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")

    
    def test1NoDataEntered(self):
        # 1. Kliknij „Login”
        zaloguj_a = self.driver.find_element(By.ID, "login-button")
        zaloguj_a.click()
        # OCZEKIWANY REZULTAT
        # 1. Użytkownik otrzymuje informację „Epic sadface: Username is required” 
        # a) Szukam wszystkich komunikatów o błędzie użytkownika
        user_error_messages= self.driver.find_elements(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        # b) Sprawdzam, czy liczba komunikatów o błędzie wynosi 1
        self.assertEqual(1, len(user_error_messages))
        # c) Sprawdzam, czy treść komunikatu jest widoczna i brzmi "Epic sadface: Username is required"
        self.assertEqual("Epic sadface: Username is required", user_error_messages[0].text)
        
        sleep(3)
    
    def test2WrongUsernameEntered(self):
        # 1. Wpisz bledny Username 
        username_input = self.driver.find_element(By.NAME, "user-name")
        username_input.send_keys("standard.user")
        # 2. Wpisz poprawny password
        dalej_a = self.driver.find_element(By.ID, "password")
        dalej_a.send_keys("secret_sauce")
        # 3. Kliknij "Login"
        zaloguj_a = self.driver.find_element(By.ID, "login-button")
        zaloguj_a.click()
        # OCZEKIWANY REZULTAT
        # 1. Użytkownik otrzymuje informację „Epic sadface: Username and password do not match any user in this service”
        # a) Szukam wszystkich komunikatów o błędzie użytkownika
        user_error_messages= self.driver.find_elements(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        # b) Sprawdzam, czy liczba komunikatów o błędzie wynosi 1
        self.assertEqual(1, len(user_error_messages))
        # c) Sprawdzam, czy treść komunikatu jest widoczna i brzmi "Epic sadface: Username and password do not match any user in this service"
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", user_error_messages[0].text)
        
        sleep(3)

    def test3WrongPasswordEntered(self):
        # 1. Wpisz Username 
        username_input = self.driver.find_element(By.NAME, "user-name")
        username_input.send_keys("standard_user")
        # 2. Wpisz bledny password
        dalej_a = self.driver.find_element(By.ID, "password")
        dalej_a.send_keys("secret.sauce")
        # 3. Kliknij "Login"
        zaloguj_a = self.driver.find_element(By.ID, "login-button")
        zaloguj_a.click()
        # OCZEKIWANY REZULTAT
        # 1. Użytkownik otrzymuje informację „Epic sadface: Username and password do not match any user in this service” 
        # a) Szukam wszystkich komunikatów o błędzie użytkownika
        user_error_messages= self.driver.find_elements(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        # b) Sprawdzam, czy liczba komunikatów o błędzie wynosi 1
        self.assertEqual(1, len(user_error_messages))
        # c) Sprawdzam, czy treść komunikatu jest widoczna i brzmi "Epic sadface: Username and password do not match any user in this service"
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", user_error_messages[0].text)
        
        sleep(3)

    def test4Login(self):
        # 1. Wpisz poprawny Username 
        username_input = self.driver.find_element(By.NAME, "user-name")
        username_input.send_keys("standard_user")
        # 2. Wpisz poprawny password
        dalej_a = self.driver.find_element(By.ID, "password")
        dalej_a.send_keys("secret_sauce")
        # 3. Kliknij "Login"
        zaloguj_a = self.driver.find_element(By.ID, "login-button")
        zaloguj_a.click()
        # OCZEKIWANY REZULTAT
        # 1. Uzytkownik zostaje przekierowany do sklepu
        # 2. Sprawdzam, czy jestem na stronie o tytule "Products"
        text = self.driver.find_element(By.CLASS_NAME, "title").text 
        assert "products" in text.lower()
        print("TEST PASSED : LOGIN SUCCESSFUL")
    
    def test5AddProductsToCart(self):
        # 1. Wpisz poprawny Username 
        username_input = self.driver.find_element(By.NAME, "user-name")
        username_input.send_keys("standard_user")
        # 2. Wpisz poprawny password
        dalej_a = self.driver.find_element(By.ID, "password")
        dalej_a.send_keys("secret_sauce")
        # 3. Kliknij "Login"
        zaloguj_a = self.driver.find_element(By.ID, "login-button")
        zaloguj_a.click()
        # 4. Wybierz z listy "Onesie"
        onesie_find = self.driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
        onesie_find.click()
        # 5. Dodaj do koszyka
        add_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_to_cart.click()
        # 6. Wroc do produktow aby dodac kolejny produkt
        back_to_products = self.driver.find_element(By.ID, "back-to-products")
        back_to_products.click()
        # 7. Wybierz z listy "Bike Light"
        bike_light_find = self.driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
        bike_light_find.click()
        # 8. Dodaj do koszyka
        add_to_cart2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart2.click()

        # OCZEKIWANY REZULTAT
        # W koszyku znajduja sie dwa produkty
        # 1. Sprawdzam, czy w koszyku znajduja sie dwa produkty
        cart_value = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert "2" in cart_value.text
        print("TEST PASSED : ADD TO CART", "\n")

        # 9. Przejdz do koszyka
        show_cart = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        show_cart.click()

        # OCZEKIWANY REZULTAT
        # Zostaje przekierowany na strone koszyka
        # 1. Sprawdzam, czy jestem na stronie o tytule "Your Cart"
        text = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert "your cart" in text.lower()
        print("TEST PASSED: INSIDE CART")
        # 2. Sprawdzam, czy w koszyku znajduja sie dokladnie te dwa produkty, ktore zostaly dodane
        text = self.driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div').text
        assert "sauce labs onesie" in text.lower()
        print("TEST PASSED: CORRECT ITEM ADDED")

        text = self.driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div').text
        assert "sauce labs bike light" in text.lower()
        print("TEST PASSED: CORRECT ITEM ADDED")

    def test6RemoveProductFromCart(self):
        # 1. Wpisz poprawny Username 
        username_input = self.driver.find_element(By.NAME, "user-name")
        username_input.send_keys("standard_user")
        # 2. Wpisz poprawny password
        dalej_a = self.driver.find_element(By.ID, "password")
        dalej_a.send_keys("secret_sauce")
        # 3. Kliknij "Login"
        zaloguj_a = self.driver.find_element(By.ID, "login-button")
        zaloguj_a.click()
        # 4. Wybierz z listy "Onesie"
        onesie_find = self.driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
        onesie_find.click()
        # 5. Dodaj do koszyka
        add_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_to_cart.click()
        # 6. Wroc do produktow aby dodac kolejny produkt
        back_to_products = self.driver.find_element(By.ID, "back-to-products")
        back_to_products.click()
        # 7. Wybierz z listy "Bike Light"
        bike_light_find = self.driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
        bike_light_find.click()
        # 8. Dodaj do koszyka
        add_to_cart2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart2.click()

        # OCZEKIWANY REZULTAT
        # W koszyku znajduja sie dwa produkty
        # 1. Sprawdzam, czy w koszyku znajduja sie dwa produkty
        cart_value = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert "2" in cart_value.text
        print("TEST PASSED : ADD TO CART", "\n")

        # 9. Przejdz do koszyka
        show_cart = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        show_cart.click()

        # OCZEKIWANY REZULTAT
        # Zostaje przekierowany na strone koszyka
        # 1. Sprawdzam, czy jestem na stronie o tytule "Your Cart"
        text = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert "your cart" in text.lower()
        print("TEST PASSED: INSIDE CART")
        # 2. Sprawdzam, czy w koszyku znajduja sie dokladnie te dwa produkty, ktore zostaly dodane
        text = self.driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div').text
        assert "sauce labs onesie" in text.lower()
        print("TEST PASSED: CORRECT ITEM ADDED")

        text = self.driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div').text
        assert "sauce labs bike light" in text.lower()
        print("TEST PASSED: CORRECT ITEM ADDED")

        # 10. Usuwam produkt z koszyka
        remove_from_cart = self.driver.find_element(By.ID, "remove-sauce-labs-bike-light")
        remove_from_cart.click()

        # OCZEKIWANY REZULTAT
        # W koszyku znajduje sie tylko jeden produkt
        # 1. Sprawdzam, czy w koszyku znajduje sie juz tylko jeden produkt
        cart_value = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert "1" in cart_value.text
        print("TEST PASSED : ONE ITEM REMOVED", "\n")

    def test7Checkout(self):
        # 1. Wpisz poprawny Username 
        username_input = self.driver.find_element(By.NAME, "user-name")
        username_input.send_keys("standard_user")
        # 2. Wpisz poprawny password
        dalej_a = self.driver.find_element(By.ID, "password")
        dalej_a.send_keys("secret_sauce")
        # 3. Kliknij "Login"
        zaloguj_a = self.driver.find_element(By.ID, "login-button")
        zaloguj_a.click()
        # 4. Wybierz z listy "Onesie"
        onesie_find = self.driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
        onesie_find.click()
        # 5. Dodaj do koszyka
        add_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_to_cart.click()
        # 6. Wroc do produktow aby dodac kolejny produkt
        back_to_products = self.driver.find_element(By.ID, "back-to-products")
        back_to_products.click()
        # 7. Wybierz z listy "Bike Light"
        bike_light_find = self.driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
        bike_light_find.click()
        # 8. Dodaj do koszyka
        add_to_cart2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart2.click()

        # OCZEKIWANY REZULTAT
        # W koszyku znajduja sie dwa produkty
        # 1. Sprawdzam, czy w koszyku znajduja sie dwa produkty
        cart_value = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert "2" in cart_value.text
        print("TEST PASSED : ADD TO CART", "\n")

        # 9. Przejdz do koszyka
        show_cart = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        show_cart.click()
        # 10. Checkout
        checkout_btn = self.driver.find_element(By.ID, 'checkout')
        checkout_btn.click()
        # OCZEKIWANY REZULTAT
        # 1. Uzytkownik znajduje sie na stronie "checkout"
        text = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert "checkout: your information" in text.lower()
        print("TEST PASSED: CHECKOUT")

        # 11. Uzupelniam wymagane pola aby zlozyc zamowienie
        first_name_input = self.driver.find_element(By.ID, "first-name")
        first_name_input.send_keys("Bolek")

        last_name_input = self.driver.find_element(By.ID, "last-name")
        last_name_input.send_keys("Lolek")

        zip_code_input = self.driver.find_element(By.ID, "postal-code")
        zip_code_input.send_keys("192837")
        # 12. Kontynuuje zakonczenie zamowienia
        continue_btn = self.driver.find_element(By.ID, 'continue')
        continue_btn.click()

        # OCZEKIWANY REZULTAT
        # 1. Uzytkownik zostaje przekierowany na strone podsumuwujaca zamowienie
        # 2. Sprawdzam, czy jestem na stronie "checkout: overview"
        text = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert "checkout: overview" in text.lower()
        print("TEST PASSED: CHECKOUT: OVERVIEW")

        # 13. Finalizuje zamowienie
        finish_btn = self.driver.find_element(By.ID, 'finish')
        finish_btn.click()
        
        # OCZEKIWANY REZULTAT
        # Finalizacja sie powiodla
        # 1. Uzytkownik otrzymuje wiadomosc "Thank you for your order!"
        order_message= self.driver.find_element(By.CLASS_NAME, 'complete-header')
        self.assertEqual("Thank you for your order!", order_message.text)
        print("PROJECT FINISHED")
        

    def tearDown(self):
        self.driver.quit()

# Jeśli uruchomiono ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main(verbosity=2)