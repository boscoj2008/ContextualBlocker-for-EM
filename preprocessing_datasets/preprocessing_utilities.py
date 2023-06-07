#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper: Blocking Techniques for Entity Linkage: A Semantics-Based Approach

@author: Fabio Azzalini, Songle Jin, Marco Renzi, Letizia Tanca
"""
import pandas as pd
import itertools
import os

def get_labels_by(path, label):
    table = load_csv(path)
    return table[label]

def load_csv(path):
    dirname = os.path.dirname(__file__)
    path_dataset = os.path.join(dirname, path)
    return pd.read_csv(path_dataset, sep=';', parse_dates=True, dtype=str, error_bad_lines=False)

def createEntities(table):
    entities = dict()
    for ent in set(table['class']):
        entities[ent] = list(table[table['class'] == ent].index)
    return entities

def createPairs(entities):
    pairs = set()
    for val in entities:
        for x in itertools.combinations(entities[val], 2):
            ordered_pair = tuple(sorted(x))
            pairs.add(ordered_pair)
    return pairs
    
# REMOVE blank leading and trailing chars
def lrstrip(table, attr):
    return table.loc[:, attr].str.lstrip().str.rstrip()
    

# SET empty values to default value 'unk'
def setEmpty(table, attr):
    return table[attr].replace(',', 'unk', inplace=True)

# SET all to lowercase
def setLowercase(table, attr):
    return table[attr].str.lower()
