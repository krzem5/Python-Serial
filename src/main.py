import serial
import sys
import time



for p in serial.serial_list():
	print(f"{p['name']} -> {p['vid']}:{p['pid']}")
ss=serial.serial_open("COM3",9600,5000)
et=time.time()+5
while (True):
	l=serial.serial_queue_len(ss)
	if (l>0):
		sys.__stdout__.write(str(serial.serial_read(ss,l),"utf-8"))
		sys.__stdout__.flush()
	else:
		serial.serial_write(ss,bytes(str(time.time()),"utf-8")+b"\n")
	if (time.time()>=et):
		break
serial.serial_close(ss)
print("\nEND!")
