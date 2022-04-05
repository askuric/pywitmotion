import time
import numpy as np
import struct

def interpret_data(data):
    s = data
    cmd = chr(int(data.hex()[:2], 16))
    print(cmd,int(data.hex()[:2],16),ascii(50),ord('P'))

    if cmd == 'P': # 0x50
        print("time")
    elif cmd == 'Q': # 0x51 
        print("accel")        
    elif cmd == 'R': # 0x52
        print("gyro")
    elif cmd == 'S': # 0x53
        print("angle")
        print(np.array(struct.unpack('<HHH', data[1:7]))/32768*180 )
        #print(int(data[4:6],16),int(data[6:8],16),int(data[8:10],16),int(data[10:12],16))
    elif cmd == 'T': # 0x54
        print("mag")    
    elif cmd == 'U': # 0x55
        print("status")    
    elif cmd == 'V': # 0x56
        print("press")    
    elif cmd == 'W': # 0x57
        print("lonlat")    
    elif cmd == 'X': # 0x58
        print("gpsv")    
    elif cmd == 'Y': # 0x59
        print("quat")
        print(int(data.hex()[4:6],16),int(data.hex()[6:8],16),int(data.hex()[8:10],16),int(data.hex()[10:12],16))
    elif cmd == 'Z': # 0x5a
        print("sn")

def get_angle(data):
    cmd = struct.unpack('c', data[0:1])[0]
    if len(data) < 7:
        return 
    if cmd == b'S': # 0x53
        return np.array(struct.unpack('<hhh', data[1:7]))/32768*180 
    return None

def get_quaternion(data):
    cmd = struct.unpack('c', data[0:1])[0]
    if len(data) < 9:
        return None
    if cmd == b'Y':
        q = np.array(struct.unpack('<hhhh', data[1:9]))/32768.0
        return np.array([q[1],q[2],q[3],q[0]])
    return None

def wrap_angle(angle):
    angle[angle>180] = angle[angle>180] - 360
    return angle