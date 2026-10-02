#!/bin/bash
import socket
import paramiko
import threading

class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        print(f"{username}:{password}")
        return paramiko.AUTH_FAILED


def handle_con(client_sock):
    transport = paramiko.Transport(client_sock)
    server_key = paramiko.RSAKey.from_private_key_file("key")
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0',2222))
    server_socket.listen(100)

    while True:
        client_sock, client_addr = server_socket.accept()
        print(f"connection from {client_addr[0]}:{client_addr[1]}")
        t = threading.Thread(target=handle_con,args=(client_sock,))
        t.start()

if __name__ == "__main__":
    main()
