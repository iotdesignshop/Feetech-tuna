# Feetech-tuna
Cross Platform Feetech Servo Tuner Tool

## Important Notices and Safety Information

_This tool is provided as a utility tool for reading and setting registers and parameters from Feetech servos. You should ensure
that you understand the usage and function of these registers before manipulating them. It may be possible to damage your servo motor
or to render it unusable if you set these registers incorrectly. Consult the Feetech factory documentation for your servos before 
using the tool!_

## Installation

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
(TBD)

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
python tuna.py <URT-1 Serial Port> --baudrate <baudrate (optional - defaults to 1000000 which is used for Feetech STS servos)
```

On Linux, with default baudrate, this might look something like this:
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
(TBD)

### Determining Serial Port on Windows
(TBD)

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

### ListRegs Command

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

### Exit Command

This will exit Feetech-tuna and shut down the serial port properly.

```
>> exit
```





