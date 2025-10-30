import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")
    msg_history = []
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        msg = client_socket.recv(1024).decode()
        msg_history.append(msg)
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {msg}")

        client_socket.send('\n'.join(msg_history).encode())
        client_socket.close()


if __name__ == '__main__':
    server()
