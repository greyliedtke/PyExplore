import socket

# Define the IP range to scan
ip_range = "192.168.0."
start_ip = 1
end_ip = 255

# Loop through the IP range and attempt to connect to each IP address
for i in range(start_ip, end_ip + 1):
    ip = ip_range + str(i)
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5)  # Set a timeout for the socket

    # Attempt to connect to the IP address on a specific port (e.g., port 80 for HTTP)
    result = sock.connect_ex((ip, 80))

    # Check if the connection was successful (0 indicates success)
    if result == 0:
        print(f"Host {ip} is up and port 80 is open")
    else:
        print(f"Host {ip} is down")

    sock.close()  # Close the socket