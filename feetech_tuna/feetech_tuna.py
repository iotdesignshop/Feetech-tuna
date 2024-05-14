import sys
import os

cd = os.path.dirname(__file__)
scservo_path = os.path.join(cd, 'SCServo_Python')
sys.path.append(scservo_path)

from scservo_sdk import *


servoRegs = [
    { "name": "ID", "addr": SMS_STS_ID, "size": 1, "type": "uint8" },
    { "name": "Model", "addr": SMS_STS_MODEL_L, "size": 2, "type": "uint16"},
    { "name": "Baudrate", "addr": SMS_STS_BAUD_RATE, "size": 1, "type": "uint8" },
    { "name": "Min Angle Limit", "addr": SMS_STS_MIN_ANGLE_LIMIT_L, "size": 2, "type": "uint16" },
    { "name": "Max Angle Limit", "addr": SMS_STS_MAX_ANGLE_LIMIT_L, "size": 2, "type": "uint16" },
    { "name": "CW Dead Zone", "addr": SMS_STS_CW_DEAD, "size": 1, "type": "uint8" },
    { "name": "CCW Dead Zone", "addr": SMS_STS_CCW_DEAD, "size": 1, "type": "uint8" },
    { "name": "Offset", "addr": SMS_STS_OFS_L, "size": 2, "type": "uint16" },
    { "name": "Mode", "addr": SMS_STS_MODE, "size": 1, "type": "uint8" },
    { "name": "Torque Enable", "addr": SMS_STS_TORQUE_ENABLE, "size": 1, "type": "uint8" },
    { "name": "Acceleration", "addr": SMS_STS_ACC, "size": 1, "type": "uint8" },
    { "name": "Goal Position", "addr": SMS_STS_GOAL_POSITION_L, "size": 2, "type": "uint16" },
    { "name": "Goal Time", "addr": SMS_STS_GOAL_TIME_L, "size": 2, "type": "uint16" },
    { "name": "Goal Speed", "addr": SMS_STS_GOAL_SPEED_L, "size": 2, "type": "uint16" },
    { "name": "Lock", "addr": SMS_STS_LOCK, "size": 1, "type": "uint8" },
    { "name": "Present Position", "addr": SMS_STS_PRESENT_POSITION_L, "size": 2, "type": "uint16" },
    { "name": "Present Speed", "addr": SMS_STS_PRESENT_SPEED_L, "size": 2, "type": "uint16" },
    { "name": "Present Load", "addr": SMS_STS_PRESENT_LOAD_L, "size": 2, "type": "uint16" },
    { "name": "Present Voltage", "addr": SMS_STS_PRESENT_VOLTAGE, "size": 1, "type": "uint8" },
    { "name": "Present Temperature", "addr": SMS_STS_PRESENT_TEMPERATURE, "size": 1, "type": "uint8" },
    { "name": "Moving", "addr": SMS_STS_MOVING, "size": 1, "type": "uint8" },
    { "name": "Present Current", "addr": SMS_STS_PRESENT_CURRENT_L, "size": 2, "type": "uint16" }
]



class FeetechTuna:
    def __init__(self):
        pass

    def openSerialPort(self, port, baudrate) -> bool:
        print("Opening serial port: " + port)

        self.porthandler = PortHandler(port)
        self.packetHandler = sms_sts(self.porthandler)
        if (self.porthandler.openPort()):
            print("Opened port. Configuring baudrate...")
        else:
            print("Failed to open the port")
            return False
        
        if (self.porthandler.setBaudRate(baudrate)):
            print("Baudrate set to " + str(baudrate))
        else:
            print("Failed to set baudrate")
            return False
        
        print("Serial port opened successfully")

        return True

    def closeSerialPort(self) -> None:
        if (self.porthandler):
            self.porthandler.closePort()
            print("Closed port")

    def listServos(self):
        result = []
        print("Scanning servo bus. Please wait...")
        for servo in range(0, 254):
            model_number, comm_result, error = self.packetHandler.ping(servo)
            print('.', end='', flush=True)
            if comm_result == COMM_SUCCESS:
                result.append({ "id" : servo, "model": model_number})
        print()
        return result
    
    def listRegs(self, servoId):
        result = []
        for reg in servoRegs:
            value, comm_result, error = self.packetHandler.readTxRx(servoId, reg["addr"], reg["size"])
            if (reg["size"] == 2):
                value = self.packetHandler.scs_tohost(self.packetHandler.scs_makeword(value[0], value[1]), 15)
            else:
                value = value[0]
            if comm_result == COMM_SUCCESS:
                result.append({ "name": reg["name"], "addr" : reg["addr"], "value": value })
        return result
            

