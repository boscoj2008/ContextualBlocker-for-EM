#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A Graph-Based Blocking Approach for Entity Matching Using Contrastively Learned Embeddings 
Authors: John Bosco Mugeni & Toshiyuki Amagasa 
Institute: University of Tsukuba (ibaraki, Japan).

Published: ACM SIGAPP Applied Computing Review (Feb 2023)
"""



from .algorithm_utilities import clusterArray_to_blockDict
import community as community_louvain
import networkx as nx
from cdlib import algorithms
import pandas as pd
import time 


def vec_2_graph(vectors, N):
    import networkx as nx
    from sklearn.neighbors import kneighbors_graph
    # build the graph which is full-connected
    mat = kneighbors_graph(vectors, N, metric='cosine', mode='distance', include_self=True, n_jobs=-1)
    mat.data = 1 - mat.data  # to similarity
    g = nx.from_scipy_sparse_matrix(mat, create_using=nx.Graph())
    print(nx.info(g))
    return g 


def all_in_one_clusteriser(vectors, clusteriser="louvian", N=10 ):
    """"clusterise using louvian, leiden, markov, or eig """
    import pandas as pd
    
    if clusteriser == 'louvian':
        print("using louvian clusterizer")
        start = time.time()
        graph = vec_2_graph(vectors, N) # init graph
        end = time.time()
        dif = end - start        
        print("graph constructed in {:.2f} seconds".format(dif))
        
        start_blocking = time.time()
        partition = community_louvain.best_partition(graph, random_state=42)
        end_blocking = time.time()
        dif = end_blocking - start_blocking
        print("blocking completed in {:.2f} seconds".format(dif))
        
        return clusterArray_to_blockDict(partition.values())
    
    if clusteriser == 'leiden':
        print("using leiden clusterizer")
        start = time.time()
        graph = vec_2_graph(vectors, N) # init graph
        end = time.time()
        dif = end - start
        print("graph constructed in {:.2f} seconds".format(dif))
        
        start_blocking = time.time()
        comms = algorithms.leiden(graph)
        comms = comms.communities
        end_blocking = time.time()
        dif = end_blocking - start_blocking
        print("blocking completed in:", dif,' seconds')
        comms = dict(sorted({item:list_id for list_id, l in enumerate(comms) for item in l}.items()))
        return clusterArray_to_blockDict(pd.Series(comms).values) 
    

   



    
