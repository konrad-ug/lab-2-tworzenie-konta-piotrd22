# bank-app

| Termin oddania | Punkty |
| ------- | ------ |
| 26.10.2022 23:00 | 10 |

Przekroczenie terminu o n zajęć wiąże się z karą:

- punkty uzyskania za realizację zadania są dzielone przez 2^n.

Zadanie:
Jesteś osobą odpowiedzialną za stworzenie corowej funkcjonalności aplikacji bankowej.
Pierwszym zadaniem jest stworzenie funkcjonalności zakładania konta bankowego. W celu zoptymalizowania procesu developmentu wybierasz metodologie TDD.

Zaimplementuj poniże funkcjonalności używając TDD. 

Feature 1:
System powinien umożliwiać stworzenie osobistego konta bankowego.
Konto powinno posiadać następujące parametry:
- imię i nazwisko właściciela (podawane w trakcie tworzenia konta)
- saldo (początkowe saldo dla wszystkich kont wynosi 0)

*Podpowiedź*:
Proszę sklonować swoje repozytorium:
```
git clone nazwa_repo
```
Proszę stworzyć swojego feature brancha
```
git checkout -b feature_1
```
Aby wykonać testy:
```
python3 -m unittest
```
Testy będą "czerwone" z errorem:
*__init__() takes 1 positional argument but 3 were given'*

Proszę dopisać kod w pliku Konto.py tak aby testy przechodziły.
**Proszę zrobić push swojej zmiany oraz stworzyć PR do brancha main oraz przypisać mnie (konrad-sol) do review.**

Proszę zastanowić się co można poprawić w naszym teście.
Proszę zastanowić się nad testem do kolejnego feature.
Gdy PR będzie zmergowany proszę stworzyć nowego brancha:
```
git checkout -b lab2
```
Po zakończeniu wszystkich features proszę ponownie wystawić PR.

Feature 2:
Okazało się że imię i nazwisko nie są unikatowymi wartościami pozwalającymi zidentyfikować właściciela konta.
Musimy dodać zmienną wejściową niezbędną do tworzenia konta - numer PESEL. Konto powinno przechowywać podany PESEL.

Feature 3:
Problem: Nasi użytkownicy podają zbyt krótkie lub zbyt długie numery PESEL. 
Musimy dodać funkcjonalność która sprawdzi czy podany PESEL ma dokładnie 11 znaków. Jeżeli nie ma, w zmiennej *pesel* powinniśmy przechowywać informację "Niepoprawny pesel!"

Feature 4:
By zwiększyć sprzedaż zakładanych kont zespół sprzedaży rozpoczął akcje promocyjną.
Jeżeli przy zakładaniu konta użytkownik poda kod rabatowy w postaci PROM_XYZ (gdzie XYZ to dowolne znaki) do nowo utworzonego konta dodajemy 50zł. Kod rabatowy nie jest obowiązkowy do założenia konta.

*Podpowiedź*:
Jeżeli zmienna nie jest obowiązkowa – w definicji konstruktora możemy ustawić default na None.

Proszę skupić się możliwych scenariuszach, napisać testy i na końcu dokonać zmian w programie.

Feature 5:
W rezultacie akcji promocyjnej konto było bardzo popularne wśród seniorów. Bank jest teraz na skraju bankructwa. Musimy ograniczyć promocję – od teraz tylko osoby urodzone po roku 1960 roku życia otrzymają 50zł przy zakładaniu konta z uzyciem kodu.

Podpowiedź:
Rok urodzenia ukryty jest w numerze PESEL.

Znów, proszę najpierw skupić się na testach.

Podpowiedź 2: Może warto dodatkową logikę przenieść do oddzielnej metody?

Po zakończeniu proszę wystawić PR i przypisać mnie do review.
By uzyskać pełną ilość punktów (10) PR powinien być wsyatwiony do 26.10.2022 do godziny 23:00.

 
