import socket
import threading

#  Server setting
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 4444))
server.listen(4)
server.settimeout(1)

clients = []
def client_handler(client, addr):

    # Initialize username
    client.send("Enter username:".encode())
    username = client.recv(1024).decode()
    client.send(f"Welcome {username}!".encode())


    while True:
        message = client.recv(1024)

        if not message:
            clients.remove(client)
            print(f"{username} ({addr}) disconnected.")
            break
        else:
            for user in clients:
                if user is not client:
                    user.send(username.encode() + b": " + message)


try:
    while True:
        try:
            client,addr = server.accept()
        except socket.timeout:
            continue

        clients.append(client)
        print(f"{addr} connected.")

        threading.Thread(
            target=client_handler,
            args=(client,addr),
            daemon=True
        ).start()

except KeyboardInterrupt:
    print("\nServer Stopped.")

finally:
    server.close()