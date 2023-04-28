import socket
import dotenv


def handle_client(server_ip_: str, server_port_: int):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((server_ip_, server_port_))

    print(f"[CLIENT SOCK] {client_sock}")
    print("[CLIENT ADDRESS] {}:{}".format(*client_sock.getsockname()))

    print('[CONNECTION] Connection with {}:{}'.format(*(server_ip_, server_port_)))
    while True:
        mess = input("YOU: ")
        message = mess.encode()
        client_sock.sendall(message)
        data = client_sock.recv(16)
        print(f'SERVER: {data.decode()}')


server_ip = dotenv.get_key('.env', 'LOCAL_IP')
server_port = int(dotenv.get_key('.env', 'LOCAL_PORT'))

handle_client(server_ip, server_port)
