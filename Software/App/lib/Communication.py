import serial
import serial.tools.list_ports

# Function to get the first available serial port
def get_serial_port():
    ports = serial.tools.list_ports.comports()
    if not ports:
        raise Exception("NO serial ports found!!!")
    return ports[0].device  

# Initialize the serial connection to the UniTest Board
UniTest_Board = serial.Serial(get_serial_port(), 9600, timeout=1)

# Function to open the serial port (if needed)
def open_port():
    if not UniTest_Board.is_open:
        UniTest_Board.open()

# Function to close the serial port (if needed)
def close_port():
    if UniTest_Board.is_open:
        UniTest_Board.close()

#Function to check if the port is open
def is_port_open():
    return UniTest_Board.is_open

# Function to write data to the UniTest Board
def send_command(data):
    UniTest_Board.write(data)

# Function to read data from the UniTest Board
def read():
    if UniTest_Board.in_waiting > 0:
        return UniTest_Board.readline().decode(errors="ignore").strip()
    return None

# Function to flush input and output buffers
def flush():
    UniTest_Board.flushInput()
    UniTest_Board.flushOutput() 

# Function to get the number of bytes in the input buffer
def in_waiting():
    return UniTest_Board.in_waiting 

