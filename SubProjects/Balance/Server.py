# echo-server.py

import socket
import json

HOST = ""  # accept all
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data: conn.send(b"thanks")
            json_data = data.decode('utf-8')
            try:
                # Deserialize JSON data to dictionary
                received_data = json.loads(json_data)
                print(received_data)
            except:
                pass
