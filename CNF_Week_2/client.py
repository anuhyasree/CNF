import socket
import threading


def main():
    host = '127.0.0.1'
    port = 5002
    s = socket.socket()
    s.connect((host, port))
    threading.Thread(target = recovary, args = (s, )).start()

    while True:
        message = input("message")
        s.send((message).encode())
    s.close()

def recovary(s):
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)
        if data!="ROLLNUMBER-NOTFOUND":
            ans=input("Ans:")
            s.send(ans.encode())

if __name__ == '__main__':
        main()