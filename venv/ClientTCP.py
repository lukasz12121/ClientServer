import socket, pickle, sys


host = 'localhost'
port = 64000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Podłączam się do serwera")
sock.connect((host, port))
print("Podłączono")
while True:
  print("Podaj liczbę")
  liczba = eval(input("Podaj liczbę całk. lub -1 żeby zakończyć: "))
  if liczba == -1:
    break
  data_string = pickle.dumps(liczba)
  sock.send(data_string)
sock.close()
