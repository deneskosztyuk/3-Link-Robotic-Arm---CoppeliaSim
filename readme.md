# Robotic Manipulator Kinematics Simulation

## Project Overview

This project implements **forward and inverse kinematics** solutions for a multi-link planar manipulator using **CoppeliaSim** and **Python**. The simulation demonstrates fundamental robotics concepts by analyzing the relationship between joint angles and end-effector positions in robotic arms.

## Objective

The primary goal is to understand and implement the mathematical relationships that govern robotic manipulator movement:
- **Forward Kinematics**: Determine end-effector position from known joint angles
- **Inverse Kinematics**: Calculate required joint angles to reach a desired end-effector position

## Technologies Used

- **CoppeliaSim**: 3D robot simulation environment
- **Python**: Mathematical calculations and control logic
- **NumPy**: Numerical computations
- **Math Library**: Trigonometric calculations for kinematic equations

## Features

### ✅ Forward Kinematics Implementation
- Calculates end-effector position (x, y coordinates) from joint angles
- Uses trigonometric relationships for 2D planar movement
- Real-time visualization in CoppeliaSim
<img width="504" height="211" alt="image" src="https://github.com/user-attachments/assets/e1970008-0835-4d09-a591-47acad33e9ae" />


### ✅ Inverse Kinematics Solution
- Computes required joint angles for desired end-effector positions
- Handles geometric and trigonometric calculations
- Supports both analytical and numerical solution methods

### ✅ 3D Simulation Environment
- Interactive CoppeliaSim scene with kinematic manipulator
- Visual representation of joint movements and end-effector trajectories
- Dynamic mode simulation with proper joint configurations
<img width="630" height="354" alt="image" src="https://github.com/user-attachments/assets/edd27ff1-6573-40bf-8972-a44fc5ef9d35" />


### ✅ Python Integration
- Seamless communication between Python scripts and CoppeliaSim
- Object handling for manipulator components (base, joints, links)
- Automated sequence control for demonstrating various configurations
<img width="409" height="154" alt="image" src="https://github.com/user-attachments/assets/88434226-eece-4a67-b9a9-f7d2251807e9" />
<img width="416" height="243" alt="image" src="https://github.com/user-attachments/assets/5ffc5e76-d9a8-417d-a587-2b43cbb8d90f" />



## Technical Implementation

The project addresses key robotics challenges:

- **Mathematical Modeling**: Implementation of kinematic equations using trigonometry
- **Simulation Integration**: Connecting Python control algorithms with 3D visualization
- **Joint Control**: Programming sequential movements and angle calculations
- **Coordinate Systems**: Managing 2D planar coordinates and transformations

## Learning Outcomes

This project demonstrates proficiency in:
- **Robotics Fundamentals**: Understanding of manipulator kinematics
- **Mathematical Modeling**: Application of trigonometry and geometry in robotics
- **Simulation Software**: Experience with professional robotics simulation tools
- **Python Programming**: Implementation of numerical algorithms and system integration

## How to Run

1. **Prerequisites**: Install CoppeliaSim and Python with NumPy
2. **Setup**: Load the provided CoppeliaSim scene file
3. **Execute**: Run the Python script to control the manipulator
4. **Interact**: Observe forward/inverse kinematics calculations in real-time
5. **Exit**: Press 'Q' to quit the simulation

## Applications

This foundational work in robotic kinematics has applications in:
- Industrial automation and manufacturing
- Robotic arm control systems
- Path planning and trajectory optimization
- Educational robotics and simulation
