import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.11', 5000))

    try:
        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Server response: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
