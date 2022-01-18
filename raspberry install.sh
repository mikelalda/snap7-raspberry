#!/bin/sh

# Install telegram-bot
git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive

cd python-telegram-bot

python3 setup.py install



# Install Snap7
wget http://sourceforge.net/projects/snap7/files/1.2.1/snap7-full-1.2.1.tar.gz/download

cd snap7-iot-arm-1.4.2/build/unix/

sudo make -f arm_v7_linux.mk all

sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/lib/libsnap7.so

sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/lib/libsnap7.so

sudo pip install python-snap7



