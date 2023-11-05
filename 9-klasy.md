## Ćwiczenia do wykonania

1. Stwórz klasę Firewall, która będzie przechowywać zasady (reguły) dotyczące ruchu sieciowego i oceniać, czy próba połączenia jest dozwolona, czy zablokowana. Klasa powinna mieć następujące metody:
    - \_\_init__(self): inicjalizacja listy zasad (każda zasada to słownik z kluczami: 'ip', 'port' i 'akcja'),
    - dodaj_zasade(self, ip, port, akcja): dodaje nową zasadę do firewalla,
    - sprawdz_polaczenie(self, ip, port): zwraca True, jeśli połączenie jest dozwolone, False jeśli zablokowane, na podstawie zasad.

2. Zaprojektuj klasę Uzytkownik, która będzie zarządzać informacjami o użytkownikach w systemie bezpieczeństwa. Klasa powinna posiadać:
    - Atrybuty instancji: login, haslo, email, poziom_dostepu (gdzie poziom dostępu określa uprawnienia użytkownika w systemie, np. 'admin', 'user', 'guest').
    - Metodę \_\_init__(self, login, haslo, email, poziom_dostepu): inicjalizacja nowego użytkownika z podanymi atrybutami,
    - Metodę zmien_haslo(self, stare_haslo, nowe_haslo): metoda pozwala zmienić hasło użytkownika, ale tylko jeśli stare haslo jest poprawne,
    - Metodę \_\_str__(self): która zwraca informacje o użytkowniku (bez hasła) w czytelnej formie,
    - Metodę zresetuj_haslo(self): resetuje hasło do domyślnej wartości, np. "Password123", i zwraca informację o zmianie.
    
### Przykładowe rozwiązania

#### Zadanie 1.
```python
class Firewall:
    def __init__(self):
        self.zasady = []

    def dodaj_zasade(self, ip, port, akcja):
        self.zasady.append({'ip': ip, 'port': port, 'akcja': akcja})

    def sprawdz_polaczenie(self, ip, port):
        for zasada in self.zasady:
            if zasada['ip'] == ip and zasada['port'] == port:
                return zasada['akcja'] == 'dozwol'
        return False  # Domyślnie blokujemy połączenie, jeśli nie ma zasady

# Testowanie klasy
fw = Firewall()
fw.dodaj_zasade("192.168.1.1", "22", "dozwol")
fw.dodaj_zasade("192.168.1.2", "80", "zablokuj")

print(fw.sprawdz_polaczenie("192.168.1.1", "22"))
print(fw.sprawdz_polaczenie("192.168.1.2", "80")) 

```

```
True
False
```

#### Zadanie 2.
```python
class Uzytkownik:
    def __init__(self, login, haslo, email, poziom_dostepu):
        self.login = login
        self.haslo = haslo
        self.email = email
        self.poziom_dostepu = poziom_dostepu

    def zmien_haslo(self, stare_haslo, nowe_haslo):
        if self.haslo == stare_haslo:
            self.haslo = nowe_haslo
            return "Hasło zostało zmienione."
        else:
            return "Błędne stare hasło, nie zmieniono hasła."

    def __str__(self):
        return f"Użytkownik: {self.login}, Email: {self.email}, Poziom dostępu: {self.poziom_dostepu}"

    def zresetuj_haslo(self):
        self.haslo = "Password123"
        return "Hasło zostało zresetowane do domyślnej wartości."

# Testowanie klasy
uzytkownik = Uzytkownik("jnowak", "BezpieczneHaslo123", "jnowak@example.com", "user")
print(uzytkownik)
print(uzytkownik.zmien_haslo("BezpieczneHaslo123", "NoweHaslo321"))
print(uzytkownik.zresetuj_haslo())

```

```
Użytkownik: jnowak, Email: jnowak@example.com, Poziom dostępu: user
Hasło zostało zmienione.
Hasło zostało zresetowane do domyślnej wartości.
```
