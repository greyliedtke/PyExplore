# echo-client.py

import socket
import json

HOST = "192.168.0.16"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def send_d(dd):
    # Serialize the dictionary to JSON
    json_data = json.dumps(dd)

    # Send the JSON data
    s.send(json_data.encode('utf-8'))
    
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    print(data)
    send_d({"pi": 9, "angle": 3})
    send_d({"pi": 15, "angle": 31})
