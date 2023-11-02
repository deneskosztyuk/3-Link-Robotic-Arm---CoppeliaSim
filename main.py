import numpy as np
import math
import sim
import time
print("Program started")
sim.simxFinish(-1)
clientID = sim.simxStart("127.0.0.1", 19997, True, True, 5000, 5)
if clientID != -1:
    print("Connected to remote API server")
else:
    print("Failed to connect to remote API")
    print("Program exited")
res, objs = sim.simxGetObjects(clientID, sim.sim_handle_all,sim.simx_opmode_blocking)
if res == sim.simx_return_ok:
    print('Number of objects in the scene: ', len(objs))
else:
    print('Remote API function call returned with error code: ', res)
time.sleep(2)
# Getting object handle
opMode = sim.simx_opmode_blocking
errorCode, base = sim.simxGetObjectHandle(clientID, "Base", opMode)
errorCode, pendulum1 = sim.simxGetObjectHandle(clientID, "Pendulum1", opMode)
errorCode, pendulum2 = sim.simxGetObjectHandle(clientID, "Pendulum2", opMode)
errorCode, pendulum3 = sim.simxGetObjectHandle(clientID, "Pendulum3", opMode)
errorCode, Joint1 = sim.simxGetObjectHandle(clientID, "joint1", opMode)
errorCode, Joint2 = sim.simxGetObjectHandle(clientID, "joint2", opMode)
errorCode, Joint3 = sim.simxGetObjectHandle(clientID, "joint3", opMode)
# Forward kinematics
theta1 = 90
theta2 = -90
theta3 = 45
theta1 = math.radians(theta1)
theta2 = math.radians(theta2)
theta3 = math.radians(theta3)
#Move joint1
for i in range(1, 100 + 1):
    J1a = i * 0.01 * theta1;
    errorCode = sim.simxSetJointPosition(clientID, Joint1, J1a, opMode)
#Move joint2
for i in range(1, 100 + 1):
    J2a = i * 0.01 * theta2;
    errorCode = sim.simxSetJointPosition(clientID, Joint2, J2a, opMode)
#Move joint3
for i in range(1, 100 + 1):
    J3a = i * 0.01 * theta3;
    errorCode = sim.simxSetJointPosition(clientID, Joint3, J3a, opMode)
sim.simxFinish(clientID)