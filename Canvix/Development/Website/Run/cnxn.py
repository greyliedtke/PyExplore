import socket

# Define Raspberry Pi's IP address and port
HOST = '192.168.0.23'  # Replace with Raspberry Pi's IP address
PORT = 65432                      # Port on which the server is listening

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    # Send a command to the server
    command = "your_command_here"  # Replace with your command
    s.sendall(command.encode('utf-8'))
    print(f"Sent command: {command}")
