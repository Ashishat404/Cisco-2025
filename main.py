

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
