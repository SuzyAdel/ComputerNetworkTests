import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.11', 5000))  # Ensure this IP matches your server's IP address
    server_socket.listen(1)
    print("TCP Server is listening on port 5000 at IP 192.168.1.10")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")
        conn.sendall(b"Echo: " + data)

    conn.close()

if __name__ == "__main__":
    start_server()
