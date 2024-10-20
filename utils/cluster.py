#聚类
from scipy.linalg import eigvals

from io_metric import *
# from Tst import *
import numpy as np
import scipy.linalg as sl
import numpy.matlib
from numpy import linalg as la
from CONST import *
import vulnerability
from sympy import symbols

from vulnerability import constraint


def half_metric(A):
    # 求矩阵-1/2次方
    # v 为特征值    Q 为特征向量
    v, Q = la.eig(A)
    V = np.diag(v ** (-0.5))
    T = Q * V * la.inv(Q)
    return T


def eig(C, L):
    C = np.array(C)
    L = np.array(L)
    lhs = np.multiply(C.transpose(), L, C)
    rhs = np.multiply(C.transpose(), C)
    # lam = symbols('lam')
    # lhs_rhs = lhs - lam*rhs
    # lam_result = 1
    lamb, u = sl.eigh(lhs, rhs, eigvals_only = False, type = 1)
    return lamb[:2], [list(u[:,i]/sum(u[:,i])) for i in range(2)]


def cluster():

    # 此处是解算潮流过后的W，D
    D_half = half_metric(D)
    L = np.matlib.identity(BUS_NUM) - np.dot(D_half, W, D_half)
    C = constraint(wind_speed=36)
    lamb, u = eig(C, L)
    u_1 = np.multiply(C, u[:,0])
    u_2 = C@u[:,1]
    



if __name__ == '__main__':
    A = np.random.rand(2, 2)
    B = np.random.rand(2, 2)
    m, n = eig(A,B)
    print(m, n[:,0], n)