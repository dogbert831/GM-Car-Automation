import time
import serial
import subprocess
import sys
# Enter the mac address of the MX Bluetooth here
subprocess.call("sudo rfcomm bind 0 MA:CO:FD:EV:IC:E4", shell=True)

# Serial settings, this will most likely stay the same
ser = serial.Serial(
    port='/dev/rfcomm0',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
# The lines you will most likely need to edit are AT CP and AT SH
ser.isOpen()

print 'Executing Command...'
ser.write("ATR0 \r\n")
# Turn off responses
time.sleep(0.5)
ser.write("ATAL \r\n")
# Allow long messages to be sent on the CAN Bus
time.sleep(0.5)
# Switch to 11-bit
ser.write("STP 61 \r\n")
time.sleep(0.5)
# Wake the CAN Bus up
ser.write("STCSWM 2 \r\n")
time.sleep(0.5)
ser.write("AT SH 621 \r\n")
time.sleep(0.5)
ser.write("01 FF FF FF FF 00 00 00 \r\n")
time.sleep(0.5)
# The CAN Bus is awake, switch back to normal 29-bit
ser.write("STCSWM 3 \r\n")
time.sleep(0.5)
ser.write("STP 62 \r\n")
time.sleep(0.5)
# insert your found code here
ser.write("AT CP 00 \r\n")
time.sleep(0.5)
# insert more of your found code here
ser.write("AT SH 00 00 00 \r\n")
time.sleep(0.5)

if sys.argv[1] == "start":
	ser.write("02 01 \r\n")
	time.sleep(0.3)
	ser.write("02 0B \r\n")
	time.sleep(0.3)
elif sys.argv[1] == "stop":
	ser.write("02 01 \r\n")
	time.sleep(0.3)
	ser.write("02 0C \r\n")
	time.sleep(0.3)
elif sys.argv[1] == "lock":
        ser.write("02 01 \r\n")
        time.sleep(0.3)
elif sys.argv[1] == "unlock":
        ser.write("02 02 \r\n")
        time.sleep(0.3)
elif sys.argv[1] == "unlock_all":
        ser.write("02 03 \r\n")
        time.sleep(0.3)
elif sys.argv[1] == "panic":
        ser.write("02 07 \r\n")
        time.sleep(0.3)
elif sys.argv[1] == "trunk":
        ser.write("02 15 \r\n")
        time.sleep(0.3)
else :
	print "No Argument"
	
ser.write("STCSWM 0 \r\n")
time.sleep(0.5)
ser.close()
time.sleep(0.5)
subprocess.call("sudo rfcomm release 0", shell=True)
