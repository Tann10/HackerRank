#!/bin/python3

from collections import defaultdict
from heapq import heappop, heappush
import os


def shortestReach(n, edges, s):

    # create a null dict
    graph = defaultdict(list)

    # get keys from dict edges and add into graph dict having structure as
    # {start_node : [(dist, edge node)]} for all the nodes
    for (u, v), w in edges.items():
        print(u, v, w)
        graph[u].append((w, v))
        graph[v].append((w, u))
    print(graph)

    # create a visited list with all false values as default
    visited = [False for _ in range(n + 1)]

    # create distance list with inf values as default
    distance = [float("inf") for _ in range(n + 1)]

    # assign distance as zero for the start node
    distance[s] = 0

    # create a min structure with tuple as (distance of startnode, startnode)
    # min always stort value in ascending order by default
    minHeap = [(distance[s], s)]

    # till the heap is not empty continue with the loop
    while minHeap:

        # pop lowest dist and edge node
        d, u = heappop(minHeap)

        # if the node is already visted cont with the next heap value
        if visited[u]:
            continue

        # if its not visited assign true value for the node
        visited[u] = True

        # get all the connected noted to the current node
        for w, v in graph[u]:

            # if the connected node is not visited already and distance to that node is min that the already min value
            if not visited[v] and distance[v] > d + w:

                # add the min value in the node
                distance[v] = d + w

                # push the pair of distance and node to the heap
                heappush(minHeap, (distance[v], v))

    # delete start node values as its not expected to return
    del distance[s]
    del distance[0]

    # if the distance value is still inf then the node is not connected hence return -1
    return [-1 if d == float("inf") else d for d in distance]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n, m = map(int, input().split())

        edges = dict()

        for _ in range(m):
            u, v, w = map(int, input().rstrip().split())

            if (u, v) in edges:
                edges[(u, v)] = min(edges[(u, v)], w)
            elif (v, u) in edges:
                edges[(v, u)] = min(edges[(v, u)], w)
            else:
                edges[(u, v)] = w

        print(edges)

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()