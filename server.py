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
                conn.sendall(b"Serwer: Odebralem Twoja wiadomosc!")

run_server()