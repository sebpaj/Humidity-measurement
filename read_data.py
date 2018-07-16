import serial
import time
import datetime as dt

ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

while True:
    data = []
    try:
        with open("output.txt","a") as f:
            ser_bytes = ser.readline()
            decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            with open("output.txt", "a") as file:
                file.write(decoded_bytes+" "+dt.datetime.now().strftime('%H:%M:%S')+"\n")
        time.sleep(300)
    except:
        print("Keyboard Interrupt")
