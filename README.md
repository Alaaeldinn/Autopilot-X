# Autopilot-X

## Overview

This project implements a self-driving car using the Carla simulator. Carla is an open-source simulator that provides a realistic environment for autonomous driving research and development.

## Requirements

- Carla Simulator (version X.X.X)
- Python (version X.X)
- Dependencies (list them with versions)

## Installation

1. Clone this repository: `git clone https://github.com/Alaaeldinn/Autopilot-X.git`
2. Install Carla Simulator following the instructions on their official documentation.
3. Install Python dependencies: `pip install -r requirements.txt`

## Usage

1. Launch Carla Simulator.
2. Navigate to the project directory.
3. Run the self-driving car script: `python self_driving_car.py`

## Components

### Perception

- Utilizes sensors (camera, lidar, radar) to perceive the environment.
- Implements computer vision algorithms for object detection and recognition.

### Planning

- Generates a high-level path based on the perceived environment.
- Considers traffic rules, obstacles, and destination.

### Control

- Converts the planned path into low-level control commands.
- Interfaces with the simulator to control the car's acceleration, steering, and braking.

## Configuration

Adjust parameters in the configuration file (`config.yaml`) to fine-tune the system based on your requirements.

## License

This project is licensed under the XYZ License - see the [LICENSE](LICENSE) file for details.
