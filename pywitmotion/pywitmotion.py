import numpy as np
import struct


# datasheet with bluetooth protocol
# https://drive.google.com/file/d/1vpPqaVdSLzlPhd9YFE3bjj0f75XtiSyO/view
def get_acceleration(data):
    if len(data) < 7:
        return None
    cmd = struct.unpack('c', data[0:1])[0]
    if cmd == b'Q': # 0x54
        return np.array(struct.unpack('<hhh', data[1:7]))/32768.0*16.0
    return None

def get_gyro(data):
    if len(data) < 7:
        return None
    cmd = struct.unpack('c', data[0:1])[0]
    if cmd == b'R': # 0x54
        return np.array(struct.unpack('<hhh', data[1:7]))/32768.0*2000.0
    return None

def get_magnetic(data):
    if len(data) < 7:
        return None
    cmd = struct.unpack('c', data[0:1])[0]
    if cmd == b'T': # 0x54
        return np.array(struct.unpack('<hhh', data[1:7]))
    return None

def get_angle(data):
    if len(data) < 7:
        return 
    cmd = struct.unpack('c', data[0:1])[0]
    if cmd == b'S': # 0x53
        return np.array(struct.unpack('<hhh', data[1:7]))/32768.0*180.0 
    return None

def get_quaternion(data):
    if len(data) < 9:
        return None
    cmd = struct.unpack('c', data[0:1])[0]
    if cmd == b'Y':
        q = np.array(struct.unpack('<hhhh', data[1:9]))/32768.0
        return np.array([q[1],q[2],q[3],q[0]])
    return None