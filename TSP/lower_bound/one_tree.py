import numpy as np

from lower_bound import mst

class OneTreeMst:
    def __init__(self):
        pass
    def cal_one_tree_mst(self,dist: np.ndarray):
        one_tree_max = 0
        n = dist.shape[0]
        mst_ = mst.MST()
        print(f"MST cost : {round(mst_.cal_mst([],dist),2)}")
        for i in range(n):
            mst_cost = round(mst_.cal_mst([i],dist),2)
            #TODO: calculate 2 minimum edges
            w1 = 10**9
            w2 = 10**9
            for wei in dist[i]:
                if wei>0.001:
                    if wei<w1:
                        w2 = w1
                        w1 = wei
                    elif wei<w2:
                        w2 = wei

            one_tree_cost = round(mst_cost+w1+w2,2)
            one_tree_max = max(one_tree_cost,one_tree_max)
            # print(mst_cost,one_tree_cost)

        return one_tree_max




