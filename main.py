

import os
import networkx as nx
import matplotlib.pyplot as plt

def parse_configs(config_dir):
    configs = {}
    for root, _, files in os.walk(config_dir):
