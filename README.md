# pywitmotion
A python pip package for parsing witmotion IMU messages

![](./datasheet/image.jpg)

Find the datasheet at [BWT901CL Datasheet.pdf](./datasheet/BWT901_Datasheet.pdf)


## Instalation
```
pip install git+https://github.com/askuric/pywitmotion.git
```

## Code examples
Code example using `pybluez`

```python
import pywitmotion as wit
import bluetooth

# set your device's address
imu = "00:0C:BF:02:1E:40"

# Create the client socket
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect((imu, 1))

msgs_num = 0
while msgs_num < 100:
    data = socket.recv(1024)
    # split the data into messages
    data = data.split(b'U') 
    for msg in data:
        q = wit.get_quaternion(msg)
        # q = wit.get_magnetic(msg)
        # q = wit.get_angle(msg)
        # q = wit.get_gyro(msg)
        # q = wit.get_acceleration(msg)
        if q is not None:
            msgs_num = msgs_num+1
            print(q)
socket.close()
```

Code example using `pyserial`
```python
import serial
import pywitmotion as wit

connected = False
port = '/dev/rfcomm0'
baud = 115400

with serial.Serial(port, baud, timeout=5) as ser:
    s = ser.read()

    msgs_num = 0
    while msgs_num < 100:
        start = time.time()
        s = ser.read_until(b'U')
        q = wit.get_quaternion(msg)
        # q = wit.get_magnetic(msg)
        # q = wit.get_angle(msg)
        # q = wit.get_gyro(msg)
        # q = wit.get_acceleration(msg)
        if q is not None:
            msgs_num = msgs_num+1
            print(q)
```
