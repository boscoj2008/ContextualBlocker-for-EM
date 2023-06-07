#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper: Blocking Techniques for Entity Linkage: A Semantics-Based Approach

@author: Fabio Azzalini, Songle Jin, Marco Renzi, Letizia Tanca
"""
def clusterArray_to_blockDict(clusters):
    blocks = {}
    for index, value in enumerate(clusters):
        if value in blocks.keys():
            blocks[value].append(index)
        else:
            blocks[value] = list()
            blocks[value].append(index)
    return blocks
