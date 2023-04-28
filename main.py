import socket
import os
import dotenv

if __name__ == '__main__':
    host = dotenv.get_key('.env', 'LOCAL_IP')
    port = int(dotenv.get_key('.env', 'LOCAL_PORT'))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'[SERVER SOCKET] {server_socket}')
    print(f'[PROCESS ID] {os.getpid()}')

    server_socket.bind((host, port))
    server_socket.listen(2)

    while True:
        # Бесконечно обрабатываем входящие подключения
        print(f"[LISTENING] Server is listening on {host}:{port}")
        client_socket, client_addr = server_socket.accept()
        print('[NEW CONNECTION] Connection with {}:{}'.format(*client_socket.getpeername()))
        try:
            while True:
                data = client_socket.recv(16)
                print(f'CLIENT: {data.decode()}')
                mess = input("YOU: ")
                mess = mess.encode()
                client_socket.sendall(mess)

        except ConnectionAbortedError:
            print("[CLOSE CONNECTION] with {}:{}".format(*client_socket.getsockname()))
