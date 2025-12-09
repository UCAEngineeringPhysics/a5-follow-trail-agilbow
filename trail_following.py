from encoded_motor_driver import EncodedMotorDriver
from time import sleep
from math import pi
from machine import Pin

# SETUP
emd_left = EncodedMotorDriver(driver_ids=(15, 13, 14), encoder_ids=(10, 11))
emd_right = EncodedMotorDriver(driver_ids=(16, 18, 17), encoder_ids=(19, 20))
STBY = Pin(12, Pin.OUT)

# CONSTANTS
r = 0.025  # wheel radius
i = 98.5  # gear ratio
CPR = 28  # counts per revolution
L = 0.12  # wheel axle length
l = L / 2  # wheel axle length / 2
drev = (2 * pi) * r  # distance per revolution



# VARIABLES
d = None  # distance the wheel needs to travel
nrev_d = None  # number of revolutions based on distance d
theta = None  # angle in radians
s = None  # arc length
nrev_s = None  # number of revolutions based on arc length s



# LOOP
STBY.on()

# First straight line

d = 0.75
nrev_d = d / drev
C = nrev_d * CPR * i
# print(C)

while True:
    if emd_left.encoder_counts >= C:		 #and emd_right.encoder_counts <= -C
        emd_left.stop()
        emd_right.stop()
        sleep(3)
        break
    else:
        emd_left.forward(0.5)
        emd_right.forward(0.5)
#         print(emd_left.encoder_counts)
#         print(emd_right.encoder_counts)

emd_left.encoder_counts = 0
emd_right.encoder_counts = 0

# First turn

theta = pi / 2
s = l * theta
nrev_s = s / drev
C = (nrev_s * CPR * i) / 1.1
#print(C)

while True:
    if emd_left.encoder_counts <= -C:		# and emd_right.encoder_counts <= C
        emd_left.stop()
        emd_right.stop()
        sleep(1)
        break
    else:
        emd_left.backward(0.5)
        emd_right.forward(0.5)
#         print(emd_left.encoder_counts)
#         print(emd_right.encoder_counts)

emd_left.encoder_counts = 0
emd_right.encoder_counts = 0

# Second straight line

d = 0.5
nrev_d = d / drev
C = nrev_d * CPR * i

while True:
    if emd_left.encoder_counts >= C:		 #and emd_right.encoder_counts <= -C
        emd_left.stop()
        emd_right.stop()
        sleep(3)
        break
    else:
        emd_left.forward(0.5)
        emd_right.forward(0.5)
#         print(emd_left.encoder_counts)
#         print(emd_right.encoder_counts)

emd_left.encoder_counts = 0
emd_right.encoder_counts = 0

# Second turn

theta = (1.5 * pi)
s = l * theta
nrev_s = s / drev
C = (nrev_s * CPR * i) + 56
#print(C)

while True:
    if emd_left.encoder_counts >= C:		# and emd_right.encoder_counts <= C
        emd_left.stop()
        emd_right.stop()
        sleep(1)
        break
    else:
        emd_right.backward(0.5)
        emd_left.forward(0.5)
#         print(emd_left.encoder_counts)
#         print(emd_right.encoder_counts)

emd_left.encoder_counts = 0
emd_right.encoder_counts = 0

# Third straight line

d = 0.51
nrev_d = d / drev
C = nrev_d * CPR * i

while True:
    if emd_left.encoder_counts >= C:		 #and emd_right.encoder_counts <= -C
        emd_left.stop()
        emd_right.stop()
        sleep(3)
        break
    else:
        emd_left.forward(0.5)
        emd_right.forward(0.5)
#         print(emd_left.encoder_counts)
#         print(emd_right.encoder_counts)

emd_left.encoder_counts = 0
emd_right.encoder_counts = 0

# Third turn

theta = 1.107
s = l * theta
nrev_s = s / drev
C = (nrev_s * CPR * i)
#print(C)

while True:
    if emd_left.encoder_counts <= -C:		# and emd_right.encoder_counts <= C
        emd_left.stop()
        emd_right.stop()
        sleep(1)
        break
    else:
        emd_left.backward(0.5)
        emd_right.forward(0.5)
#         print(emd_left.encoder_counts)
#         print(emd_right.encoder_counts)

emd_left.encoder_counts = 0
emd_right.encoder_counts = 0

# Last straight line

d = 0.559
nrev_d = d / drev
C = nrev_d * CPR * i

while True:
    if emd_left.encoder_counts >= C:		 #and emd_right.encoder_counts <= -C
        emd_left.stop()
        emd_right.stop()
        sleep(3)
        break
    else:
        emd_left.forward(0.5)
        emd_right.forward(0.5)
#         print(emd_left.encoder_counts)
#         print(emd_right.encoder_counts)

emd_left.encoder_counts = 0
emd_right.encoder_counts = 0

