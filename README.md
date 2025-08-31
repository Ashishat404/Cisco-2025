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
3. 
