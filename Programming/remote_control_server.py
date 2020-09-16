import socket
import keyboard
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 8080
maxConn = 999
IP = 'LAPTOP-4CCTQVLJ'

s.bind((IP,Port))
s.listen(0)
print("Server started at"+IP+" on port "+str(Port))

(client_socket,adr) = s.accept()

print('New connection made!')
while True:
    if keyboard.is_pressed('w'):
        client_socket.send(bytes("W","utf-8"))
        print('sent W')
        sleep(0.05)
    elif keyboard.is_pressed('a'):
        client_socket.send(bytes("A","utf-8"))
        print('sent A')
        sleep(0.05)
    elif keyboard.is_pressed('d'):
        client_socket.send(bytes("D","utf-8"))
        print('sent D')
        sleep(0.05)
    elif keyboard.is_pressed('s'):
        client_socket.send(bytes("S","utf-8"))
        print('sent S')
        sleep(0.05)
    elif keyboard.is_pressed('q'):
        client_socket.send(bytes("Q","utf-8"))
        print('sent Q')
        sleep(0.05)
    elif keyboard.is_pressed('e'):
        client_socket.send(bytes("E","utf-8"))
        print('sent E')
        sleep(0.05)
    elif keyboard.is_pressed('z'):
        client_socket.send(bytes("Z","utf-8"))
        sleep(0.05)
        print('sent Z')
    elif keyboard.is_pressed('m'):
        client_socket.send(bytes("M","utf-8"))
        print('sent M')
        print('breaking')
        break
