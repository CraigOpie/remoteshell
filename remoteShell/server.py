#!/usr/bin/env python3
"""
author = "Craig Opie"
author_email = "craigopie@gmail.com"
name = "remoteShell"
version = "1.0.0"
description = "A reverse shell used to connect the client to a server."

"""
import socket
import sys
import subprocess


# Create a Socket
def create_socket():
    """ This function creates a socket and handles exceptions.

    Public Attributes:
        host (str): Used to store the host name.
        port (int): Used to store the port number for use.
        s (obj): Used to create a new instance for the socket.
    Raises:
        msg (error): Used to identify socket errors.
    """
    try:
        global host
        global port
        global s
        host = "localhost"
        port = 88
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    """ This function binds the socket to the host and handles exceptions.
    Raises:
        msg (error): Used to identify socket errors.
    """
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)
def socket_accept():
    """ This function creates the server/client connection. """
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands to client
def send_commands(conn):
    """ This function sends commands to the client shell.

    Args:
        conn (obj): Instance of connection to client.
    """
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(88),"utf-8")
            print(client_response, end="")


# Main function
def main():
    """ This function handles process flow. """
    create_socket()
    bind_socket()
    socket_accept()


# Verify program is not being called as a module
if __name__ == "__main__":
    # Clear the screen
    subprocess.call('clear', shell=True)
    main()
