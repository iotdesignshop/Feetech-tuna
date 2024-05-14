import argparse
from feetech_tuna import FeetechTuna

# Command line arts for port and baudrate
parser = argparse.ArgumentParser(description='Feetech Tuna - A tuning tool for Feetech servos')
parser.add_argument('port', type=str, help='The serial port to connect to')
parser.add_argument('--baudrate', type=int, default=1000000, help='The baudrate to use')

args = parser.parse_args()

tuna = FeetechTuna()

# Open the serial port
if tuna.openSerialPort(port=args.port, baudrate=args.baudrate):
    print("Succeeded to open the port")
else:
    print("Failed to open the serial port - " + args.port)
    print("Exiting...")
    quit()


