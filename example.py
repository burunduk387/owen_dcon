import serial
ser = serial.Serial(
    port="COM3",
    baudrate=9600,
    timeout=0.5
)
ser.close()

ser.open()
ser.write(ask_value_cmd(16, 1))
print(float(read_mv()))
