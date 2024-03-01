import numpy as np

import heapq


class MST:
    def __init__(self):
        pass

    def cal_mst(self, lis: list, dist: np.ndarray):
        vis = set(lis)
        print(dist.shape[0])
        n = dist.shape[0]
        heap = []
        heapq.heapify(heap)

        for i in range(n):
            if not i in vis:
                heapq.heappush(heap, [-1, i])
                break

        mst_tot = 0

        while len(vis) != n:
            print(heap)
            edgew, node = heapq.heappop(heap)
            if node in vis:
                continue
            if edgew!=-1:
                print(f"ed = {edgew,node}")
                mst_tot+=edgew
            vis.add(node)
            print(vis,n)
            for i, wei in enumerate(dist[node]):
                if not i in vis:
                    heapq.heappush(heap, [dist[node][i], i])
                    # break;

        return mst_tot

dist = np.array([
    [0, 2, 1, 4, 3],
    [2, 0, 3, 5, 4],
    [1, 3, 0, 6, 2],
    [4, 5, 6, 0, 7],
    [3, 4, 2, 7, 0]
])
mst_ = MST()
print(mst_.cal_mst([],dist))