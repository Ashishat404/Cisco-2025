

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
