import socket 
import time

print("Hi welcome to Banner Grabber")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(0.5)

ip = input("Enter Ip address: ")
time.sleep(0.5)
port = int(input("Type port here you want to scan: "))

print(f"attacking {ip} with port {port}...")

s.connect((ip, port))

print("<-------------------------------->")
print("Results found:", s.recv(1024))
print("Done")





