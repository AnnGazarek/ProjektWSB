# ProjektWSB
Projekt zaliczeniowy A.Gazarkiewicz

## Temat projektu: Testowanie stron internetowych z wykorzystaniem Selenium Webdriver

### Wstęp
Tematem niniejszego projektu zaliczeniowego na kierunku "Tester Oprogramowania" jest "Testowanie stron internetowych z wykorzystaniem Selenium Webdriver".
Przedmiotem testów jest poprawne działanie sklepu internetowego http://www.saucedemo.com.
Jest to strona testowa, specjalnie stworzona pod ćwiczenia testowe.
Projekt został zrealizowany pod opieką p. Kamila Musiał.

### Cel i zakres
Obszarem testów jest działanie sklepu internetowego: logowanie, dodawanie produktów do koszyka, usuwanie z koszyka oraz finalizacja zakupów.
W moich testach skupiłam się na przeanalizowaniu powyższych możliwości za pomocą testów automatycznych i w tym celu stworzyłam kilka przypadków testowych. 

### Specyfikacja
System operacyjny komputera: Windows 11 Version 22H2 22621.1702
VM:
Selenium: 3.141.0
Biblioteki: unittest, webrider, time

### Opis projektu i przypadki testowe 
Testowane są następujące funkcje: 
- logowanie nieprawidłowe (brak danych) - czy otrzymujemy wiadomość zwrotną o błędzie 
- logowanie nieprawidłowe (nieprawidłowa nazwa użytkownika) - czy otrzymujemy wiadomość zwrotną o błędzie 
- logowanie nieprawidłowe (nieprawidłowe hasło) - czy otrzymujemy wiadomość zwrotną o błędzie 
- prawidłowe logowanie (prawidłowa nazwa użytkownika oraz hasło) - czy zostajemy przekierowani do sklepu
- dodawanie dwóch wybranych produktów do koszyka - czy w koszyku znajdują się dwa produkty, oraz czy są one prawidłowe
- usuwanie jednego produktu z koszyka - czy w koszyku znajduje się już tylko jeden produkt
- finalizacja zakupu, podanie danych do wysyłki - czy zamówienie jest prawidłowe oraz czy zakupy kończą się sukcesem

Przypadki testowe wybrałam na potrzebę projektu - są oczywiście wybiórcze i jedynie zarysem możliwości przetestowania funkcjonalnego strony.
Kroki są bliżej opisane w samym kodzie. 


  
