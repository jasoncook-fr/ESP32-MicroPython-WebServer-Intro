# Getting started with Micropython on ESP32

### To follow the examples it is recommended to install Thonny (Python IDE for beginners)

For download instructions, visit [The official website](https://thonny.org "Official Thonny Website")

## Installing Micropython Firmware onto the ESP32

**Download the latest esptool software**

```shell

git clone https://github.com/espressif/esptool.git

```

**Serial library is a possible requisite for using esptool**

```shell

sudo apt-get update
sudo apt-get install python-serial python3-serial

```


**Download the necessary firmware for our board**

Visit the official micropython [download page](https://micropython.org/download/). <br />
You will notice there are many options. For most generic ESP32 devices try [this one](https://micropython.org/download/esp32/) .

Alternatively we can use wget in commandline:

```shell

# all following commands to be executed in the esptool folder

cd esptool
wget https://micropython.org/resources/firmware/esp32-20210902-v1.17.bin


```

**Connect the ESP32 to your computer and erase all existing data**

```shell

# Change USB port if necessary

./esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

```
**Program the firmware**

```shell

# Change USB port and .bin file name to match your own

./esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin

```

**Open Thonny and verify that the firmware is working**

Under Tools -> Options -> Interpreter, Choose __MicroPython(ESP32)__

![Thonny-options](images/thonny-options.png)

**If all goes well, you should see the Micropython version and date displayed in the shell window**

![Thonny-verify](images/thonny-verify.png)




