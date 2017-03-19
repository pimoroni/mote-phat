![Mote](mote-logo.png)

Drive four channels of APA102 pixels from your Raspberry Pi or Pi Zero with Mote pHAT

##Installation

**Full install ( recommended ):**

We've created a super-easy installation script that will install all pre-requisites and get your Mote up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type:

```bash
curl -sS https://get.pimoroni.com/motephat | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/motephat/`.

**Library install for Python 3:**

on Raspbian:

```bash
sudo apt-get install python3-motephat
```
other environments: 

```bash
sudo pip3 install motephat
```

**Library install for Python 2:**

on Raspbian:

```bash
sudo apt-get install python-motephat
```
other environments: 

```bash
sudo pip2 install motephat
```

In all cases you will have to enable the i2c bus.


##Documentation & Support

* Function reference - http://docs.pimoroni.com/motephat/
* GPIO Pinout - https://pinout.xyz/pinout/mote_phat
* Get help - http://forums.pimoroni.com/c/support
