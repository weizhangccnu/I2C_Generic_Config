import os
import sys
import time
import winsound
from usb_iss import UsbIss, defs
'''
@author: Wei Zhang
@date: April 13, 2020
This script as a generic I2C cofniguration software to configure I2C slave. The I2C reg configuration data is read into a xxx.dat file.
The UsbIss as I2C master deivce is used to write and read I2C slave register.
'''
#-----------------------------------------------------------------------------------#
freqency = 1000
duration = 200
#-----------------------------------------------------------------------------------#
def main():
    config_filename = "GBS20_I2C_Config.txt"
    I2C_Addr = 0x22
    Reg_Addr = []
    Reg_Val = []
    with open(config_filename, 'r') as infile:                  # read configuration file
        for line in infile.readlines():
            if len(line.split()) == 1:                          # read I2C address
                I2C_Addr = hex(int(line.split()[0], 16))
            else:                                               # read register address and value
                Reg_Addr += [int(line.split()[0], 16)]
                Reg_Val += [int(line.split()[1], 16)]

    # set usb-iss iic master device
    iss = UsbIss()
    iss.open("COM3")
    iss.setup_i2c()

    for i in range(len(Reg_Addr)):                              # write data into i2c slave
        iss.i2c.write(I2C_Addr, Reg_Addr[i], Reg_Val[i])
        time.sleep(0.02)

    read_data = []
    for i in range(len(Reg_Addr)):                              # read data from i2c slave
        read_data += [iss.i2c.read(I2C_Addr, Reg_Addr[i], 1)]
        time.sleep(0.02)

    ## compare write in data with read back data
    if Reg_Val == Reg_Val:
        print("Read back data matched with write in data")
        for i in range(3):
            winsound.Beep(freqency, duration)
            time.sleep(0.01)
    else:
        print("Read back data didn't matche with write in data")        #print reg_add, write data, read back data
        for i in range(len(Reg_Addr)):
            if Reg_Val[i] != read_data[i]:
                print(Reg_Addr[i], Reg_Val[i], read_data[i])

    print("Ok!")
#-----------------------------------------------------------------------------------#
if __name__ == '__main__':
    main()
