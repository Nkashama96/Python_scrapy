import socket

def grab_banner(ip, port):
    """
    Grabs the service banner from a specific IP and port.
    """
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection
        s.settimeout(2)
        
        # Connect to the target
        s.connect((ip, port))
        
        # Send a simple HTTP GET request to trigger a response
        s.send(b'GET / HTTP/1.1\r\nHost: ' + ip.encode() + b'\r\n\r\n')
        
        # Receive the banner (up to 1024 bytes)
        banner = s.recv(1024)
        
        print(f"Banner from {ip}:{port}\n{banner.decode().strip()}")
        
        s.close()
    except Exception as e:
        print(f"Could not grab banner from {ip}:{port} - {e}")

# Example Usage
if __name__ == "__main__":
    target_ip = "192.168.1.1" # Change to target IP
    # Scan all ports (1 to 65535)
    for target_port in range(1, 65536):
        # target_port = 80        # Change to target port
        grab_banner(target_ip, target_port)
