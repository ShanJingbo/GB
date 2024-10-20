from matplotlib.pyplot import connect

import io_metric
import numpy as np
from CONST import *
import pandapower as pp
import pandas as pd


def create_net():
    W_pre, D_pre = io_metric.io_metric()
    connect = io_metric.jsonread("connect.json")
    net = pp.create_empty_network(f_hz=50, name="net_GB")
    buses = []
    lines = []
    for i in range(len(connect['connect'])):
        name = 'bus'+str(i+1)
        buses.append(pp.create_bus(net, vn_kv=220, name=name))
    for i in range(len(connect['connect'])):
        for j in range(i-1):
            if W_pre[i][j] == 1:
                lines.append(pp.create_line(net, buses[j], buses[i]))
    return net


def solve(net):
    pp.runpm(net)


