import socket


HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        s.send(b"GET /main/test/ HTTP/1.0\r\n\r\n")
        while 69:
            data = s.recv(1024)
            if not data:
                break
            print(data.decode())

    except ConnectionRefusedError:
        print(f"Django Is Not Running On Port: {PORT} .")
