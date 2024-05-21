import serial
import time

arduino = serial.Serial(port="COM4", baudrate=9600, timeout=0.1)


def fingerprint_authentication():
    try:
        while True:
            data = arduino.readline().decode().strip()
            matchStatus = data.split(": ", 1)
            if matchStatus[0] == "Fingerprint match":
                userID = matchStatus[1]
                print(userID)
                return userID, True
            else:
                print("No Match found")
                return None, False

    except KeyboardInterrupt:
        arduino.close()
        print("Serial connection closed.")


fingerprint_authentication()
