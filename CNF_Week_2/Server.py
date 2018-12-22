import socket
import threading

clients = list()
def srvthd(c):
    while True:
        data = c.recv(1024)
        data = data.decode()

def main():
    value = int(input("Enter number: "))
    host = '127.0.0.1'
    port = 5002
    s = socket.socket()
    s.bind((host, port))
    for i in range(0, value):
        c, addr = s.accept()
        print("connecting...... " + str(addr))
        clients.append(c)
        thread = threading.Thread(target = srvthd, args = (clients[i],))
        thread.start()
    s.close()
if __name__ == '__main__':
    main()
