import socket
import sys

# Target IP address to scan
target = input("Enter the host to scan: ")
# Convert hostname to IPv4
target_ip = socket.gethostbyname(target)

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print("Scanning started at: " + str(sys.argv[0])) # Placeholder for time
print("-" * 50)

try:
    # Scan all ports (1 to 65535)
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) # Fast timeout for scanning
        
        # connect_ex returns 0 if the connection is successful
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
