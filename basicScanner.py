import socket
import sys

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# method to scan ports
def scan_ports(ip, start_port, end_port):
    open_ports = []
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Faster but might miss some ports; adjust if needed
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            sys.exit()
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")
    if not open_ports:
        print("\nNo open ports found.")
    return open_ports

# inputs
def get_input():
    ip = input("Enter IP address to scan: ").strip()
    if not is_valid_ip(ip):
        print("Invalid IP address.")
        sys.exit(1)
    try:
        start_port = int(input("Enter start port: ").strip())
        end_port = int(input("Enter end port: ").strip())
        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
            raise ValueError
        if start_port > end_port:
            print("Start port must be less than or equal to end port.")
            sys.exit(1)
    except ValueError:
        print("Invalid port number. Must be between 0 and 65535.")
        sys.exit(1)
    return ip, start_port, end_port

if __name__ == "__main__":
    ip, start_port, end_port = get_input()
    scan_ports(ip, start_port, end_port)
