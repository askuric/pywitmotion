# pywitmotion
A pip package for parsing wit motion IMU messages

```
pip install -e git+https://github.com/askuric/pywitmotion.git
```

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
    while True:
        start = time.time()
        s = ser.read_until(b'U')
        q1 = wit.get_quaternion(s)
        if q1 is not None:
            print(time.time()-start)
```