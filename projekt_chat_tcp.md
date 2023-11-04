## Projekt: Prosty Czat TCP


### Opis:
Projekt polega na stworzeniu serwera i klienta, które komunikują się przez protokół TCP. Serwer będzie nasłuchiwał na połączenia i odpowiadał na wiadomości od klienta. Jest to podstawa do zrozumienia, jak działają niskopoziomowe połączenia sieciowe. Zachodzącą komunikację, będzie można zaobserwować również w Wireshark na interfejsie `loopback0` (`127.0.0.1`).

### Przygotowanie:
- Python 3.x już zainstalowany.

### Serwer:
```python
import socket

# Ta funkcja uruchamia serwer TCP, który nasłuchuje na lokalnym adresie i porcie.
def run_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Serwer nasłuchuje na adresie {host}:{port}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Połączono z {addr}.")
            # Główna pętla serwera, która odbiera wiadomości i odpowiada.
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Wiadomość od klienta: {data.decode()}")
                # Tu można zmieniać wiadomość wysyłaną do klienta.
                conn.sendall(b"Serwer: Odebrałem Twoją wiadomość!")

run_server()
```

### Klient:
```python
import socket

# Ta funkcja uruchamia klienta TCP, który łączy się z serwerem i wysyła wiadomość.
def run_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # Wiadomość do wysłania serwerowi - można ją zmienić.
        s.sendall(b"Klient: Witaj serwerze!")
        response = s.recv(1024)
        print(f"Odpowiedź od serwera: {response.decode()}")

run_client()
```

**Uwaga:** Aby zobaczyć komunikację uruchom najpierw serwer, a potem klienta.

#### Modyfikacje:
- Zmieniaj treść wiadomości wysyłanej przez klienta, modyfikując `b"Klient: Witaj serwerze!"`.