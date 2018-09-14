import time
import serial

print "Starting program"

ser = serial.Serial('/dev/ttyAMA0', baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)
try:
    while True:
        if ser.inWaiting() > 0:
            data = ser.read()
            print data
        
except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occurs, Exiting Program"

finally:
    ser.close()
    pass
