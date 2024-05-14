import sys

sys.path.append("./SCServo_Python")
from scservo_sdk import *


class FeetechTuna:
    def __init__(self):
        pass

    def openSerialPort(self, port, baudrate) -> bool:
        print("Opening serial port: " + port)
        return True

    def closeSerialPort(self) -> None:
        pass

