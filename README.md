# Cisco-2025
# Automatic Network Topology Generation and Simulation

cisco packet tracer used for topology with routers and pc's configured. 
here I have tried to make a program for generation of topology and for simulation we haev cisco packet tracer 
so we will see it there.
## Overview
This project provides a solution for automatic network topology generation from router configuration files and manual topology creation in Cisco Packet Tracer. It demonstrates how to parse configuration files, build a network graph using Python and NetworkX, and visualize or simulate network behavior. The Packet Tracer file visually represents the same topology for practical validation and demonstration.
## Features
- Parses router configuration files to extract device and connection information
- Builds a hierarchical network topology graph using NetworkX
- Prints nodes and edges to verify the generated topology
- Provides a Packet Tracer (.pkt) file for manual topology creation and simulation
- Includes sample configuration files for testing

## Workflow of the problem statemnt :
1. Place sample configuration files in the `Conf/` directory (e.g., `Conf/R1/config.dump`).
2. Run `main.py` to parse configs and generate the network topology graph.
3.  View the printed nodes and edges to verify the topology.
4. Open the `.pkt` file in Cisco Packet Tracer to view and simulate the same topology visually.

## Files being Submitted :
- main.py: Python script for automatic topology generation
- ReadMe.txt: Project overview and instructions
- ReadMe.txt: Project overview and instructions
- simulator.py: Detailed problem statement and requirements
- AshishBhatt.pkt : its a packet tarcer file it gives us a network topology diagram with configured routers.
- validator.py 

## How to Run
1. Ensure you have Python and NetworkX installed.
2. Place your config files in the `Conf/` directory.
3. now inside Conf 
│   ├── R1/config.dump --> connects_to: R2
                           connects_to: SW1

│   ├── R2/config. --> connects_to: R1
4. Run `main.py`:
   
   python main.py

• Open `topology.pkt` in Cisco Packet Tracer to view the manual topology.

## Notes
- Each device and interface should have a unique IP address within its subnet.
- The Packet Tracer file must be opened in Cisco Packet Tracer software.
- You can expand the Python code to include validation, load management, and simulation features as needed.

```
TERMINAL OUTPUT : (this is runned in VS Code )
with virtual env. and matplotlib
                                   python -u "d:\Cisco\VIP code 2025\main.py"
Nodes: [('R1', {'type': 'router'}), ('R2', {'type': 'router'}), ('R3', {'type': 'router'}), ('Switch1', {'type': 'switch'}), ('Switch2', {'type': 'switch'}), ('PC0', {'type': 'pc'}), ('Laptop', {'type': 'laptop'}), ('PC1', {'type': 'pc'}), ('Server', {'type': 'server'})]
Edges: [('R1', 'R2', {'bandwidth': 1000}), ('R1', 'R3', {'bandwidth': 1000}), ('R1', 'Switch1', {'bandwidth': 100}), ('R2', 'R3', {'bandwidth': 1000}), ('R3', 'Switch2', {'bandwidth': 100}), ('Switch1', 'PC0', {'bandwidth': 100}), ('Switch1', 'Laptop', {'bandwidth': 100}), ('Switch2', 'PC1', {'bandwidth': 100}), ('Switch2', 'Server', {'bandwidth': 100})]
```
