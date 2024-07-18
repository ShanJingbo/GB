#输入，输出W, D, net
import scipy.io as sio
import numpy as np
import pandapower as pp
import json

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

    W = np.zeros([num_bus, num_bus])
    D = np.diag(np.ones(num_bus))
    for i in range(0,num_bus):
        for j in range(0,num_bus):
            if (j+1) in connect[i]:
                W[i][j] = 1
    for i in range(0,num_bus):
        D[i][i] = sum(W[i])
    net = pp.create_empty_network()
    return net, W, D
