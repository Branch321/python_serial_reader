import serial

test_length = 10
ser = serial.Serial('COM5',115200)
print(ser.name)
for feet_range in range(1,16):
    rssi_data = []
    ser.flushInput()
    ser.flushOutput()
    with open( "results\\distance_results_"+str(feet_range) + "_feet"+ ".txt",'w+') as file:
        for i in range(0, test_length):
            raw_serial_data = ser.readline()
            rssi_data.append(raw_serial_data.decode("utf-8").rstrip())
            print(i,end=' ')
            print(rssi_data[i])
            file.write(rssi_data[i] + '\n')
    input("Hit Enter to Start Next Test...")
    file.close()
print("DONE")