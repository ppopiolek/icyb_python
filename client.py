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