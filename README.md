# Feetech-tuna
Cross Platform Feetech Servo Tuner Tool

![IMG_8051](https://github.com/iotdesignshop/Feetech-tuna/assets/2821763/97f59ad3-29a2-4357-a35e-a58a12f00f51)


## Important Notices and Safety Information

_This tool is provided as a utility tool for reading and setting registers and parameters from Feetech servos. You should ensure
that you understand the usage and function of these registers before manipulating them. It may be possible to damage your servo motor
or to render it unusable if you set these registers incorrectly. Consult the Feetech factory documentation for your servos before 
using the tool!_

You should become familiar with the Feetech Servo Tutorial and how these operations work using the official toolset before attempting
to use this system:

https://www.feetechrc.com/Data/feetechrc/upload/file/20201127/start%20%20tutorial201015.pdf


### SCS Servo Family

This tool has currently been tested with the STS servo family from Feetech. While we do support SCS servos as well via the flags, 
this functionality is currently not well tested. If you use SCS servos with it, we would appreciate hearing about your results.

## Hardware and Connections

This tool assumes you have a Feetech URT-1 controller board powered and connected to USB on the host machine. Instructions for using the URT-1 can be found in the Feetech Tutorial link above.


## Call for Contributors

This tool is provided with a very basic text-based interface for simplicity. It would be fantastic to see these functions switched over
to a GUI-based tool at some point along with many other usability improvements. We welcome contributions to the repo and will consider all
PR's.



## Installation

### Python Versions
We recommend Python 3.10 or later. Earlier versions (such as 3.8) have some issues on Windows. 

### Python Virtual Environment
We recommend using a Python Virtual Environment to manage dependencies and packages for the project.

#### Creating a Virtual Environment on Mac/Linux
```(bash)
python3 -m venv tuna_env
```
Then, to activate your new environment:
```(bash)
source tuna_env/bin/activate
```


#### Creating a Virtual Environment on Windows
```
python -m venv tuna_env
```

Then, to activate your new environment:
```
.\tuna_env\Scripts\activate
```

### Install Requirements
With your virtual environment active:

```(bash)
pip install -r requirements.txt
```

## Launching the Tuner
Once you have all the dependencies installed, you will need to determine the serial port of your Feetech URT-1 board. There are some notes
down below on how to do this on the different host platforms (Windows/Mac/Linux).

The command line to launch the tuner is as follows:
```(bash)
python tuna.py <URT-1 Serial Port> --baudrate <baudrate (optional - defaults to 1000000 which is used for Feetech STS servos) --servofamily <sms_sts, scscl (defaults to sms_sts)>
```

On Linux, with default baudrate and connecting to STS servos, this might look something like this:
```(bash)
python tuna.py /dev/ttyUSB0
```

### Determining Serial Ports on Linux
One common issue with the Feetech URT-1 on Linux is a conflict with the brltty (Braille TTY) service on the machine. This plagues other microcontrollers and connections as well. 
BraileTTY is an accessibility tool that may not be necessary unless you are visually impaired. If you find your URT-1 device is not appearing, or is connecting and then disconnecting
from a Linux machine, you may want to have a look at this link:

[How to Stop BrailleTTY from Claiming Your Device](https://koen.vervloesem.eu/blog/how-to-stop-brltty-from-claiming-your-usb-uart-interface-on-linux/)

To determine the port name of the URT-1, you can use the following command shortly after plugging the device in:

```(bash)
sudo dmesg | tail
```

You should see output indicating the path to the device similar to this:
```
[ 1340.268906] usb 1-3: New USB device found, idVendor=1a86, idProduct=7523, bcdDevice=81.32
[ 1340.268953] usb 1-3: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[ 1340.268965] usb 1-3: Product: USB Serial
[ 1340.273726] ch341 1-3:1.0: ch341-uart converter detected
[ 1340.274513] usb 1-3: ch341-uart converter now attached to ttyUSB0
```


### Determining Serial Port on Mac
On a Mac, you can get a detailed listing of serial port devices using the following command:

```(bash)
ioreg -p IOUSB -w0 | grep -E '(Serial|USB)'
```

This should give you back a list showing the Feetech URT-1 in it somewhere, similar to this:

```
  | +-o USB Serial@14300000  <class AppleUSBDevice, id 0x105c6f4d1, registered, matched, active, busy 0 (18 ms), retain 13>
```

Then, if you run:

```
ls /dev/tty.usb*
```

You should see a device similar to the descriptor above, such as:

```
/dev/tty.usbserial-1430
```

This will be the address you give to tuna.py when launching:

```
python tuna.py /dev/tty.usbserial-1430
```




### Determining Serial Port on Windows

Device Manager is the easiest way to find the USB-SERIAL CH340 Device in Windows. To do this:

1) Press Win + X and select Device Manager.
2) Expand the "Ports (COM & LPT)" section to view the list of serial devices. Each entry should show the COM port number and device description.
These methods should help you identify and list all serial port devices connected to your Windows system via USB.

You should see an entry there called __USB-SERIAL CH340__ and it will indicate which COM port is assigned to the adapter.

Then, you can run __tuna.py__ with that argument:
```
python tuna.py COMxx
```


## Usage and Commands

Once the tuner is active and connected to to the URT-1 serial port, you can use the following commands at the prompt. 

### List Command

This will scan the servo bus for servos and report back the ID's and model numbers of all of the servos found on the bus.

```
>> list
```

The response will look like this:
```
Found 18 servos
Servo 101 - Model: 521
Servo 102 - Model: 521
Servo 103 - Model: 521
Servo 104 - Model: 521
Servo 105 - Model: 521
Servo 106 - Model: 521
Servo 107 - Model: 521
Servo 108 - Model: 521
Servo 109 - Model: 521
Servo 110 - Model: 521
Servo 111 - Model: 521
Servo 112 - Model: 521
Servo 113 - Model: 521
Servo 114 - Model: 521
Servo 115 - Model: 521
Servo 116 - Model: 521
Servo 117 - Model: 1289
Servo 118 - Model: 1289
```

### Select Command

This will select a specific servo ID to direct subsequent servo specific commands to

```
>> select <servo id>
```

### Deselect Command

This will deselect a previously selected servo
```
>> deselect
```

### List Registers Command

This will display a list of the servo register values (for a selected servo)

```
>> listregs
```

The register dump should look similar to this:
```
5 ID = 116
3 Model = 521
6 Baudrate = 0
9 Min Angle Limit = 500
11 Max Angle Limit = 3000
13 Max Temperature Limit = 70
14 Max Voltage Limit = 90
15 Min Voltage Limit = 40
16 Max Torque Limit = 1000
18 Phase = 253
19 Unloading Condition = 38
20 LED Alarm Condition = 38
21 P Coefficient = 32
22 D Coefficient = 32
23 I Coefficient = 0
24 Minimum Startup Force = 0
26 CW Dead Zone = 0
27 CCW Dead Zone = 0
28 Protection Current = 100
30 Angular Resolution = 1
31 Offset = 0
33 Mode = 0
34 Protective Torque = 20
35 Protection Time = 200
36 Overload Torque = 40
37 Speed closed loop P proportional coefficient = 10
38 Over Current Protection Time = 200
39 Velocity closed loop I integral coefficient = 200
40 Torque Enable = 0
41 Acceleration = 0
42 Goal Position = 0
44 Goal Time = 0
46 Goal Speed = 0
55 Lock = 1
56 Present Position = 513
58 Present Speed = 0
60 Present Load = 0
62 Present Voltage = 61
63 Present Temperature = 31
65 Status = 0
66 Moving = 0
69 Present Current = 0
```

### Read Register Command

Retrieves the value for a single register

```
>> readreg <address>
```

### Set Position Command

Sets servo position to a specified angle, or to min/max travel

```
>> setpos <angle>
>> setpos min
>> setpos max
```


### Unlock EEPROM Command
Most register values will only save into the EEPROM (non volatile memory) of the servo if the EEPROM is unlocked
before the value is written, and then locked afterward. Generally, you would unlock, set several values and then lock
to save the values

```
>> unlockeeprom
```

### Lock EEPROM Command
Once register values have been updated, you can lock the EEPROM to write these to flash memory to make them permanent
on the servo
```
>> lockeeprom
```

### Write Register Command
Writes a new value into a register - note that range checking and validity is not enforced by this command. It will attempt
to write whatever value you ask it into the register

```
>> writereg <address> <value>
```


### Exit Command

This will exit Feetech-tuna and shut down the serial port properly.

```
>> exit
```


## Servo Template System
We anticipate that one of the most typical use cases for Feetech-tuna will be in commissioning new servos. To assist this,
we have created a basic templating system where you can define Servo ID's and Register Values that you would like to load 
onto a servo in a single operation.

__servotemplates.py__ contains a dictionary that you can customize with your own servo templates. It's pretty straightforward:

```
# Template table for servo registers
servoTemplates = {
    101 : { 
        9 : 1500,   # Min Angle Limit 
        11 : 3000,  # Max Angle Limit
        13 : 70,    # Max Temperature Limit
        18 : 253,   # Phase
        36 : 40,    # Overload Torque
    }
}
```

The data type is just a dictionary with the key being a servo ID, and then the values being a dictionary of register addresses and the values
you would like to initialize them to. Again - ensuring these are valid values is up to you, but the tuner will attempt to write them into a 
the currently selected servo when you issue the command:

```
>> loadtemplate <template ID>
```







