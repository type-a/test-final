from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
#import csv
import datetime
import time

SERVER_HOST = "192.168.43.239"
SERVER_PORT = 502
SERVER_UNIT_ID = 8

c = ModbusClient()


def printer():
	
	''' print("Power KWH: ",abc[1],"KWH")
        print("Power KVAH: ",abc[2],"KVAH")
        print("Power KVAr: ",abc[3],"KVArH")
        print("Line Voltages:" )
        print("\tLine Voltages V RY: ",abc[4],"V")
        print("\tLine Voltages V YB: ",abc[5],"V")
        print("\tLine Voltages V BR: ",abc[6],"V")
        print()
        print("Line Current:" )
        print("\tLine Current IR: ",abc[7],"A")
        print("\tLine Current IY: ",abc[8],"A")
        print("\tLine Current IB: ",abc[9],"A")
        print()
        print("\tActive Power Consumed: ",abc[10],"KW")
        print("\tReactive Power Consumed: ",abc[11],"Kvar")
        print("\tApparent Power Consumed: ",abc[12],"KVA")
        print("Phase Voltage:")
        print("\tPhase Voltages VRN: ",abc[13],"V")
        print("\tPhase Voltages VYN: ",abc[14],"V")
        print("\tPhase Voltages VBN: ",abc[15],"V")
        print()
        print("Power Factor: ",abc[16])
        print()
        print("Frequency: ",abc[17])
        print()
        print("Load:")
        print("\tReal Power on R: ",abc[18],"KW")
        print("\tReal Power on Y: ",abc[19],"KW")
        print("\tReal Power on B: ",abc[20],"KW")
        print("\tReactive Power on R: ",abc[21],"KVAr")
        print("\tReactive Power on Y: ",abc[22],"KVAr")
        print("\tReactive Power on B: ",abc[23],"KVAr")
        print("\tApparent Power on R: ",abc[24],"KVA")
        print("\tApparent Power on Y: ",abc[25],"KVA")
        print("\tApparent Power on B: ",abc[26],"KVA") '''
	

# define modbus server host, port
c.host(SERVER_HOST)
c.port(SERVER_PORT)
c.unit_id(SERVER_UNIT_ID)

while True:
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read register (modbus function 0x03)
    if c.is_open():
        
        mydate=datetime.datetime.now()

        print (str(mydate))
        # read 54 registers at address 0, store result in regs list
        regs = c.read_input_registers(0,54)
        # if success change register value to float
        if regs:
            abc=[utils.decode_ieee(f) for f in utils.word_list_to_long(regs)]
        csvwrite=abc
        l=len(csvwrite)
        #truncate the float value upto 3 decimal places

        #Display real time values on Screen
# 	print(abc)
	
        # Time and Date Formatting
        #csvstr = datetime.datetime.strftime(mydate, '%Y/%m/%d -- %H:%M:%S')
        #abc[0]=csvstr
        #print(abc)
        #Send data to a excel file
        #myFile = open('csvexample4.csv', 'a')  
        #with myFile:  
        #   writer = csv.writer(myFile,delimiter=',',quoting=csv.QUOTE_ALL)
        #   writer.writerow(abc)

   time.sleep(0.5)
