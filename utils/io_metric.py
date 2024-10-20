#输入，输出W, D, net, bus的距离, branch数量
import scipy.io as sio
import numpy as np
import pandapower as pp
import json
from CONST import *

# 读取文件内容到字符串中
def jsonread(name):
    with open(name, 'r', encoding='utf-8') as file:
        json_str = file.read()

    # 使用json.loads()方法解析JSON字符串
    data = json.loads(json_str)
    return data

def io_metric():
    data = jsonread('GBreducednetwork.json')
    connect = jsonread('connect.json')
    connect = connect['connect']

    num_bus = len(connect)

    W_pre = np.zeros([num_bus, num_bus])
    D_pre= np.diag(np.ones(num_bus))
    for i in range(0,num_bus):
        for j in range(0,num_bus):
            if (j+1) in connect[i]:
                W_pre[i][j] = 1
    for i in range(0,num_bus):
        D_pre[i][i] = sum(W_pre[i])
    # net = pp.create_empty_network()
    # pp.create_bus(net, name="1", vn_kv="110")
    return W_pre, D_pre


def distance():
    connect = jsonread('connect.json')
    position = connect['position']
    branch_num = connect['branch_num']
    W, D = io_metric()
    distance = np.zeros([BUS_NUM, BUS_NUM])
    for i in range(0,BUS_NUM):
        for j in range(0,BUS_NUM):
            if W[i][j] == 1:
                distance[i][j] = np.sqrt(np.dot(position[i] - position[j], position[i] - position[j]))
            else:
                distance[i][j] = np.inf
    return distance, branch_num
