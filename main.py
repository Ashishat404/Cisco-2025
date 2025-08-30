

import os
import networkx as nx
import matplotlib.pyplot as plt

def parse_configs(config_dir):
    configs = {}
    for root, _, files in os.walk(config_dir):
        for file in files:
            if file.endswith(".dump"):
                device = os.path.basename(root)
                with open(os.path.join(root, file)) as f:
                    configs[device] = f.read()
    return configs


def build_topology(configs=None):
    G = nx.Graph()
    # Add routers
    G.add_node("R1", type="router")
    G.add_node("R2", type="router")
    G.add_node("R3", type="router")
    # Add switches
    G.add_node("Switch1", type="switch")
    G.add_node("Switch2", type="switch")
    # Add end devices
    G.add_node("PC0", type="pc")
    G.add_node("Laptop", type="laptop")
    G.add_node("PC1", type="pc")
    G.add_node("Server", type="server")
    
    # Connect routers to each other (fully connected)
    G.add_edge("R1", "R2", bandwidth=1000)
    G.add_edge("R2", "R3", bandwidth=1000)
    G.add_edge("R1", "R3", bandwidth=1000)

    # Connect routers to switches
    G.add_edge("R1", "Switch1", bandwidth=100)
    G.add_edge("R3", "Switch2", bandwidth=100)

    # Connect switches to end devices
    G.add_edge("Switch1", "PC0", bandwidth=100)
    G.add_edge("Switch1", "Laptop", bandwidth=100)
    G.add_edge("Switch2", "PC1", bandwidth=100)
    G.add_edge("Switch2", "Server", bandwidth=100)

    devices = {"R1": {}, "R2": {}, "R3": {}, "Switch1": {}, "Switch2": {}, "PC0": {}, "Laptop": {}, "PC1": {}, "Server": {}}
    return G, devices


def main():
