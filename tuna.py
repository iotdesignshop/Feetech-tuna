import argparse
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from feetech_tuna import FeetechTuna

# Command line arts for port and baudrate
parser = argparse.ArgumentParser(description='Feetech Tuna - A tuning tool for Feetech servos')
parser.add_argument('port', type=str, help='The serial port to connect to')
parser.add_argument('--baudrate', type=int, default=1000000, help='The baudrate to use')

args = parser.parse_args()

# Prompt history
history = InMemoryHistory()

# Create a new FeetechTuna instance
tuna = FeetechTuna()

# Welcome message
print("Welcome to Feetech Tuna!")
print("-----------------------")
print("Connecting to port: " + args.port)

# Open the serial port
if tuna.openSerialPort(port=args.port, baudrate=args.baudrate):
    print("Serial port opened successfully")
else:
    print("Failed to open the serial port - " + args.port)
    print("Exiting...")
    quit()


# Main command loop - reads commands from the user and sends them to the servo
selectedServo = None
while True:
    if (selectedServo == None):
        pmsg = ">> "
    else :
        pmsg = "(Servo " + str(selectedServo) + ") >> "

    command = prompt(pmsg, history=history)

    if command == "exit" or command == "quit":
        break
    elif command == "list":
        list = tuna.listServos()
        print("Found " + str(len(list)) + " servos")
        for servo in list:
            print("Servo " + str(servo["id"]) + " - Model: " + str(servo["model"]))
    elif command.startswith("select"):
        parts = command.split(" ")
        if len(parts) == 2:
            selectedServo = int(parts[1])
            print("Selected servo: " + str(selectedServo))
        else:
            print("Usage: select <servo_id>")
    elif command == "deselect":
        selectedServo = None
        print("Deselected servo")
    elif command == "listregs":
        if selectedServo != None:
            regs = tuna.listRegs(selectedServo)
            for reg in regs:
                print(str(reg["addr"]) + " " + reg["name"] + " = " + str(reg["value"]))
        else:
            print("No servo selected")
    elif command == "unlockeeprom":
        if selectedServo != None:
            tuna.unlockEEPROM(selectedServo)
        else:
            print("No servo selected")
    elif command == "lockeeprom":
        if selectedServo != None:
            tuna.lockEEPROM(selectedServo)
        else:
            print("No servo selected")
    elif command.startswith("writereg"):
        if selectedServo != None:
            parts = command.split(" ")
            if len(parts) == 3:
                addr = int(parts[1])
                value = int(parts[2])
                tuna.writeReg(selectedServo, addr, value)
            else:
                print("Usage: writereg <addr> <value>")
        else:
            print("No servo selected")
    elif command.startswith("readreg"):
        if selectedServo != None:
            parts = command.split(" ")
            if len(parts) == 2:
                addr = int(parts[1])
                tuna.readReg(selectedServo, addr)
            else:
                print("Usage: readreg <addr>")
        else:
            print("No servo selected")
    else:
        print("Unknown command: " + command)
        

# Close the serial port
tuna.closeSerialPort()
print("Serial port closed")
print("Exiting...")



