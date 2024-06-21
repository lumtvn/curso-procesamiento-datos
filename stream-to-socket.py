import socket
import time

# Ruta del archivo que quieres leer
file_path = 'test.txt'

# Configuración del servidor de socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 9999))
server_socket.listen(1)

print("Esperando conexiones...")
connection, address = server_socket.accept()
print(f"Conectado a {address}")

while True:
    with open(file_path, 'r') as file:
        for line in file:
            connection.send(bytes(line.strip() + "\n", "utf-8"))
            time.sleep(5)

connection.close()
