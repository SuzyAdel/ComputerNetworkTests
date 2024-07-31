import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('192.168.1.11', 5001))
    print("UDP Server is listening on port 5000")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        server_socket.sendto(b"Echo: " + data, addr)

if __name__ == "__main__":
    start_server()
