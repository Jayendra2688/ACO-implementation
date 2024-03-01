import numpy as np

import heapq


class MST:
    def __init__(self):
        pass

    def cal_mst(self, lis: list, dist: np.ndarray):
        vis = set(lis)
        n = dist.shape[0]
        heap = []
        heapq.heapify(heap)

        for i in range(n):
            if not i in vis:
                heapq.heappush(heap, [-1, i])
                break

        mst = 0

        while len(vis) != n:
            edgew, node = heapq.heappop(heap)

            if node in vis:
                continue
            if edgew != -1:
                mst += edgew
            vis.add(node)

            for i, wei in enumerate(dist[int(node)]):
                if not i in vis:
                    heapq.heappush(heap, [wei,i])

        return mst

