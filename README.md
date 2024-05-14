# Feetech-tuna
Cross Platform Feetech Servo Tuner Tool

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

### Exit Command

This will exit Feetech-tuna and shut down the serial port properly.

```
>> exit
```





