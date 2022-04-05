import socket
from utils import jsonData

class PortScan:
    portsFile = "ports.json"

    def __init__(self):
        self.open_ports = []
        self.closed_ports = []
        self.ports_info = {}
        self.remote_host = ""

    # Tarayacağı port ile ilgili bilgi alıyor. 
    def getPortsInfo(self):
        data = jsonData(PortScan.portsFile)
        self.ports_info = {int(k): v for (k,v) in data.items()}

    #Verilen inputu ip adresine dönüştürüyor. 
    @staticmethod
    def hostIPAddress(target):
        try:
            ip_addr = socket.gethostbyname(target)
        except socket.gaierror as e:
            print(f"Error occurred... {e}")
        else:
            return ip_addr

    #Taramayı yapan fonksiyon. 
    def portScanner(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)
        conn_stat = s.connect_ex((self.remote_host, port))
        if conn_stat == 0:
            self.open_ports.append(port)
        elif conn_stat != 0:
            self.closed_ports.append(port)
        s.close()

    #Parametreleri alıp sonuçları gösteren fonksiyon.
    def run(self):
        target = input("Enter destination: ")
        self.remote_host = self.hostIPAddress(target)
        self.getPortsInfo()
        for port in self.ports_info.keys():
            try:
                sPort = int(input("Enter the start port (Min-0): "))
                ePort = int(input("Enter the end port (Max-65535): "))
                for port in range(sPort, ePort + 1):
                    print(f"Scanning: {self.remote_host}:{port}")
                    self.portScanner(port)
                print("Open Ports: ")
                for port in self.open_ports:
                    print(str(port), self.ports_info[port])
                print("Closed Ports: ")
                for port in self.closed_ports:
                    print(str(port), self.ports_info[port])
            except:
                print("\nExiting...")
                break

if __name__ == "__main__":
    prtscan = PortScan()
    prtscan.run()
