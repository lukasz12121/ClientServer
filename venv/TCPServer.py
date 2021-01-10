import socket, pickle, sys


host = "localhost"
port = 64000
serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.bind((host, port))
serwer.listen()
while True:
  try:
    print("Czekam na klienta")
    conn, addr = serwer.accept()
    print("Klient podłączony")
    while True:
      data = conn.recv(4096)
      if not data:
        print('Klient został rozłączony ' + str(addr))
        break
      if data == b'':
        pass
      else:
        data_variable = pickle.loads(data)
        print('Wartość odebrana: ', str(data_variable))
  except Exception as expt:
    print(expt)
    print("Rozłączam klienta")
    break
