import scipy.io as sio
import numpy as np

# ## 将data变量保存在mat文件中data1对应的位置处
# data = np.array([1, 2, 3, 5], dtype='float32')
# sio.savemat('result.mat', {'data1': data})

## 将mat文件中data1位置对应的数据读取出来
file = sio.loadmat('GBreducednetwork.m')
# var = type('data1')
# print(var)
## 读取mat文件中的数据格式信息
info = sio.whosmat('result.mat')
print(info)
