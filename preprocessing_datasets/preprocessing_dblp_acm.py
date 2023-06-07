#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper: Blocking Techniques for Entity Linkage: A Semantics-Based Approach

@author: Fabio Azzalini, Songle Jin, Marco Renzi, Letizia Tanca
"""

import pandas as pd
import os

def clean_dblp_acm():

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname, '../source_datasets/DBLP-ACM/DBLP2.csv')
    path_dataset2 = os.path.join(dirname, '../source_datasets/DBLP-ACM/ACM.csv')
    path_dataset3 = os.path.join(dirname, '../source_datasets/DBLP-ACM/DBLP-ACM_perfectMapping.csv')

    table1 = pd.read_csv(path_dataset1,encoding="ISO-8859-1")
    # dtype_acm = {'id': int, "title": str, "authors": str, 'venue': str, 'year': str}
    table2 = pd.read_csv(path_dataset2,encoding="ISO-8859-1")
    # dtype_match = {'idDBLP': str, "idACM": int}
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1")

    table3 = table1.append(table2, ignore_index=True)
    missing_values_replace = {"id": 'unk', "title": 'unk', 'authors': 'unk', 'venue': 'unk',
                              'year': '0'}
    table3['year'] = table3['year'].astype('str')
    attributes = table3.columns.values.tolist()
    table3.fillna(value=missing_values_replace, inplace=True)

    pairs = set()

    for pair in zip(table_match['idDBLP'], table_match['idACM']):
        ordered_pair = tuple(sorted((table3.loc[table3['id'] == pair[0]].index[0], table3.loc[table3['id'] == pair[1]].index[0])))
        pairs.add(ordered_pair)


    for attr in attributes:
        table3[attr] = table3[attr].str.lower()


    table3.drop('id', axis=1, inplace=True)
    # info_task['range_set1'] = (0, len(table1.index))
    # info_task['range_set2'] = (len(table1.index), len(table3.index))

    return table3,pairs







def dirty_dblp_acm():

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname, '../source_datasets/dirty_dblp_acm_exp_data/tableA.csv')
    path_dataset2 = os.path.join(dirname, '../source_datasets/dirty_dblp_acm_exp_data/tableB.csv')
    path_dataset3 = os.path.join(dirname, '../source_datasets/dirty_dblp_acm_exp_data/Perf_matches1.csv')

    table1 = pd.read_csv(path_dataset1,encoding="ISO-8859-1") # dblp
    # dtype_acm = {'id': int, "title": str, "authors": str, 'venue': str, 'year': str}
    table2 = pd.read_csv(path_dataset2,encoding="ISO-8859-1") # acm
    # dtype_match = {'idDBLP': str, "idACM": int}
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1")

    table3 = table1.append(table2, ignore_index=True)
    missing_values_replace = {"id": 'unk', "title": 'unk', 'authors': 'unk', 'venue': 'unk',
                              'year': '0'}
    table3['year'] = table3['year'].astype('str')
    
    attributes = table3.columns.values.tolist()
    table3.fillna(value=missing_values_replace, inplace=True)

    pairs = set()

    for pair in zip(table_match['ltable_id'], table_match['rtable_id']): # ltable_id idDBLP
        ordered_pair = tuple(sorted((table3.loc[table3['id'] == pair[0]].index[0], table3.loc[table3['id'] == pair[1]].index[1])))
        pairs.add(ordered_pair)

    table3.drop('id', axis=1, inplace=True)
    for attr in attributes[1:]:
        table3[attr] = table3[attr].str.lower()




    return table3,pairs


