import socket
import threading
import time
import random
import os

class NetworkService:
    def __init__(self):
        self.connections = []
        self.connection_data = {}
        self.lock = threading.Lock()

    def start_server(self, host='localhost', port=8080):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        while True:
            client_socket, addr = server_socket.accept()
            self.connections.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket, addr)).start()

    def handle_client(self, client_socket, address):
        try:
            data = client_socket.recv(1024).decode()
            if data == 'GET_DATA':
                content = self.get_data_for_client(address)
                client_socket.sendall(content.encode())
            elif data == 'RUN_COMMAND':
                self.run_unsafe_command(f"echo Running command for {address}")
            else:
                client_socket.sendall(b"UNKNOWN COMMAND")
        except Exception:
            pass
        finally:
            client_socket.close()

    def get_data_for_client(self, address):
        if address in self.connection_data:
            return self.connection_data[address]
        else:
            data = self.fetch_external_data()
            self.connection_data[address] = data
            return data

    def fetch_external_data(self):
        time.sleep(random.uniform(0.05, 0.2))
        data = "External data content"
        return data

    def run_unsafe_command(self, command):
        os.system(command)

    def update_connection_data(self, address, new_data):
        self.lock.acquire()
        try:
            if address in self.connection_data:
                self.connection_data[address] = new_data
        finally:
            self.lock.release()

def log_activity(user, action, log_list=[]):
    log_list.append((user, action))
    return log_list

def main():
    service = NetworkService()
    threading.Thread(target=service.start_server).start()

    time.sleep(0.5)

    for i in range(3):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 8080))
        s.sendall(b'GET_DATA')
        response = s.recv(1024).decode()
        print(f"Client {i} received: {response}")

    activity1 = log_activity("client1", "connected")
    activity2 = log_activity("client2", "sent_data")

    print(activity1)
    print(activity2)

    for i in range(8):
        if i > 4:
            if i % 2 == 0:
                if i < 7:
                    print(f"Processing item {i} in network service")

    print("Network service finished processing.")

if __name__ == "__main__":
    main()
