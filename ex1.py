# -*- coding:utf-8 -*-

# bad code, q19 fail to run out the result

import numpy as np
import random

def sign(x):
    if x > 0:
        return 1
    return -1

def naive_pla(y, x, w):
    iter, update = 0, 0
    sz = 400

    while True:
        iter += 1
        error_cnt = 0

        for i in range(0, 400):
            t = np.dot(x[i], w)

            if sign(y[i]) != sign(t):
                error_cnt += 1
                update += 1

                delta = 0.5 * y[i] * x[i]
                delta.shape = (1, 5)
                w += np.transpose(delta)

        if error_cnt == 0:
            break

    return update


def false_cnt(y, x, w):
    ret = 0
    for i in range(0, 500):
        t = np.dot(x[i], w)
        if sign(y[i]) != sign(t):
            ret += 1
    return ret

def pocket_pla(y, x, w):
    iter, update = 0, 0

    w_pocket = w
    false = false_cnt(y, x, w_pocket)

    while True:
        iter += 1

        i = random.randint(0, 499)
        t = np.dot(x[i], w)

        if sign(y[i]) != sign(t):
            update += 1

            delta = y[i] * x[i]
            delta.shape = (1, 5)
            w += np.transpose(delta)

            cur_false = false_cnt(y, x, w)

            if cur_false <= false:
                # update += 1
                false = cur_false
                w_pocket = w

        if update >=50:
            break

    return w_pocket
        
def analysis(w):
    data = np.loadtxt("test1_2.dat")
    x = np.ones((500, 5))
    x[:, 1:5] = data[:, 0:4]
    y = data[:, 4:5]

    ret = false_cnt(y, x, w)
    return ret


if __name__ == '__main__':
    # data = np.loadtxt("train1_1.dat")

    # ret = 0

    # for i in range(0, 2000):
    #     print(i)
    #     np.random.shuffle(data)
    #     x = np.ones((400, 5))
    #     x[:, 1:5] = data[:, 0:4]
    #     y = data[:, 4:5]

    #     w = np.zeros((5, 1))
    #     ret += naive_pla(y, x, w)

    # print(ret/2000)

    data = np.loadtxt("train1_2.dat")
    ret = 0
    x = np.ones((500, 5))
    x[:, 1:5] = data[:, 0:4]
    y = data[:, 4:5]

    limit = 100
    for i in range(0, limit):
        print(i)

        w = np.zeros((5, 1))
        w_pocket = pocket_pla(y, x, w)

        val = analysis(w_pocket) / 500
        print(val)

        ret += val

    ret /= limit
    print(ret)
