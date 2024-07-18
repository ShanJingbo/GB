#聚类
from io_metric import *
# from Tst import *
import numpy as np
import numpy.matlib
from numpy import linalg as la
from CONST import *
import pandas as pd
import pandapower as pp


def half_metric(A):
    # 求矩阵-1/2次方
    # v 为特征值    Q 为特征向量
    v, Q = la.eig(A)
    V = np.diag(v ** (-0.5))
    T = Q * V * la.inv(Q)
    return T


W, D, net = io_metric()
D_half = half_metric(D)
L = np.matlib.identity(BUS_NUM) - np.dot(D_half, W, D_half)

