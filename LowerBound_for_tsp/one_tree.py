import numpy as np

import mst
dist = np.array([[0,3,2,4],[3,0,1,1],[2,1,0,3],[4,1,3,0]])

class OneTreeMst:
    def __init__(self):
        pass
    def cal_one_tree_mst(self,dist: np.ndarray):
        one_tree_max = 0

        mst_ = mst.MST()

        for i in range(4):
            mst_cost = mst_.cal_mst([i],dist)
            #TODO: calculate 2 minimum edges
            w1 = 10**9
            w2 = 10**9
            for wei in dist[i]:
                if wei>0.0001:
                    if wei<w1:
                        w2 = w1
                        w1 = wei
                    elif wei<w2:
                        w2 = wei

            one_tree_cost = mst_cost+w1+w2
            print(mst_cost,one_tree_cost)

        return one_tree_max




