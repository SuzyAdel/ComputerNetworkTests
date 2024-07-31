import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('server_host_ip', 5000)

    try:
        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                break
            client_socket.sendto(message.encode(), server_address)
            data, _ = client_socket.recvfrom(1024)
            print(f"Server response: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
