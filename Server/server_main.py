import socket

def server_main(host='127.0.0.1', port=5555):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")

server_main()