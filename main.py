import numpy as np
import math
import sim
import time

while True:
    print("================================================================")
    print("============Enter '1' To Perform Forward Kinematics=============")
    print("============Enter '2' To Inverse Forward Kinematics=============")
    print("=======================Enter 'Q' To Exit========================")
    print("================================================================")

    choice = input("Enter your choice here ->:")

    if choice.lower() == "q":
        break

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
    errorCode, base = sim.simxGetObjectHandle(clientID, "Stand", opMode)
    errorCode, pendulum1 = sim.simxGetObjectHandle(clientID, "Pendulum1", opMode)
    errorCode, pendulum2 = sim.simxGetObjectHandle(clientID, "Pendulum2", opMode)
    errorCode, pendulum3 = sim.simxGetObjectHandle(clientID, "Pendulum3", opMode)
    errorCode, Joint1 = sim.simxGetObjectHandle(clientID, "joint1", opMode)
    errorCode, Joint2 = sim.simxGetObjectHandle(clientID, "joint2", opMode)
    errorCode, Joint3 = sim.simxGetObjectHandle(clientID, "joint3", opMode)
    errorCode, EndEff = sim.simxGetObjectHandle(clientID, "EndEffector", opMode)
    errorCode, target = sim.simxGetObjectHandle(clientID, "Target", opMode)
    errorCode, targetPosition = sim.simxGetObjectPosition(clientID, target, base, opMode)


# Forward kinematics
    if choice == "1":
        theta1Input = int(input("Enter value for Theta 1: "))
        theta2Input = int(input("Enter value for Theta 2: "))
        theta3Input = int(input("Enter value for Theta 3: "))

        theta1 = theta1Input
        theta2 = theta2Input
        theta3 = theta3Input
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

#Inverse Kinematics
    elif choice == "2":
        # Link lengths
        L1 = 0.5
        L2 = 0.5
        L3 = 0.5

        # EF position
        xe = targetPosition[0]
        ye = targetPosition[1]
        g = np.arctan(ye/xe)
        print(targetPosition)

        x3 = xe - L3 * np.cos(g)
        y3 = ye - L3 * np.sin(g)
        r = np.sqrt(x3**2 + y3**2)
        print(r)

        if L1 + L2 > r:
            a = np.arccos((L1*L1 + L2*L2 - r*r) / (2*L1*L2))
            b = np.arccos((L1*L1 + r*r - L2*L2) / (2*L1*r))

            np.deg2rad(a)
            np.deg2rad(b)

             #elbow down
            theta1a = np.arctan2(y3, x3) - b
            theta2a = np.deg2rad(180) - a
            theta3a = g - theta1a - theta2a

            # elbow up
            #theta1b = np.arctan2(y3, x3) + b
            #theta2b = -(180-a)
            #theta3b = g - theta1b - theta2b

        # Move joint1
            for i in range(1, 100 + 1):
                J1a = i * 0.01 * theta1a
                errorCode = sim.simxSetJointPosition(clientID, Joint1, J1a, opMode)
        # Move joint2
            for i in range(1, 100 + 1):
                J2a = i * 0.01 * theta2a
                errorCode = sim.simxSetJointPosition(clientID, Joint2, J2a, opMode)
        # Move joint3
            for i in range(1, 100 + 1):
                J3a = i * 0.01 * theta3a
                errorCode = sim.simxSetJointPosition(clientID, Joint3, J3a, opMode)
        sim.simxFinish(clientID)