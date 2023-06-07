#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper: Blocking Techniques for Entity Linkage: A Semantics-Based Approach

@author: Fabio Azzalini, Songle Jin, Marco Renzi, Letizia Tanca
"""

import pandas as pd
import os

def clean_amazon_itunes():

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname, '../source_datasets/itunes_amazon/tableA.csv')
    path_dataset2 = os.path.join(dirname, '../source_datasets/itunes_amazon/tableB.csv')
    path_dataset3 = os.path.join(dirname, '../source_datasets/itunes_amazon/matches_itunes_amazon.csv')

    table1 = pd.read_csv(path_dataset1,encoding="ISO-8859-1")
    # dtype_acm = {'id': int, "title": str, "authors": str, 'venue': str, 'year': str}
    table2 = pd.read_csv(path_dataset2,encoding="ISO-8859-1")
    # dtype_match = {'idDBLP': str, "idACM": int}
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1")

    table_match["ltable_id"] = table_match["ltable_id"].astype("str")
    table_match["rtable_id"] = table_match["rtable_id"].astype("str")
     

    
    table3 = table1.append(table2, ignore_index=True)
    table3['id'] = table3['id'].astype('str')
    missing_values_replace = {"Album_Name": 'unk', 'Released': 'unk'}
    # table3['year'] = table3['year'].astype('str')
    attributes = table3.columns.values.tolist()
    table3.fillna(value=missing_values_replace, inplace=True)

    pairs = set()

    for pair in zip(table_match['ltable_id'], table_match['rtable_id']):
        ordered_pair = tuple(sorted((table3.loc[table3['id'] == pair[0]].index[0], table3.loc[table3['id'] == pair[1]].index[0])))
        pairs.add(ordered_pair)


    for attr in attributes:
        table3[attr] = table3[attr].str.lower()


    table3.drop('id', axis=1, inplace=True)
    # info_task['range_set1'] = (0, len(table1.index))
    # info_task['range_set2'] = (len(table1.index), len(table3.index))

    return table3,pairs







def dirty_amazon_itunes():

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname, '../source_datasets/dirty_itunes_amazon/tableA.csv')
    path_dataset2 = os.path.join(dirname, '../source_datasets/dirty_itunes_amazon/tableB.csv')
    path_dataset3 = os.path.join(dirname, '../source_datasets/dirty_itunes_amazon/perf_matches_itunes_amazon.csv')

    table1 = pd.read_csv(path_dataset1,encoding="ISO-8859-1")
    # dtype_acm = {'id': int, "title": str, "authors": str, 'venue': str, 'year': str}
    table2 = pd.read_csv(path_dataset2,encoding="ISO-8859-1")
    # dtype_match = {'idDBLP': str, "idACM": int}
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1")

    table_match["ltable_id"] = table_match["ltable_id"].astype("str")
    table_match["rtable_id"] = table_match["rtable_id"].astype("str")
     

    
    table3 = table1.append(table2, ignore_index=True)
    table3['id'] = table3['id'].astype('str')
    missing_values_replace = {"Song_Name": 'unk', 'Artist_Name': 'unk', 'Album_Name':'unk', 'Genre':'unk'}
    # table3['year'] = table3['year'].astype('str')
    attributes = table3.columns.values.tolist()
    table3.fillna(value=missing_values_replace, inplace=True)

    pairs = set()

    for pair in zip(table_match['ltable_id'], table_match['rtable_id']):
        ordered_pair = tuple(sorted((table3.loc[table3['id'] == pair[0]].index[0], table3.loc[table3['id'] == pair[1]].index[0])))
        pairs.add(ordered_pair)


    for attr in attributes:
        table3[attr] = table3[attr].str.lower()


    table3.drop('id', axis=1, inplace=True)
    # info_task['range_set1'] = (0, len(table1.index))
    # info_task['range_set2'] = (len(table1.index), len(table3.index))

    return table3,pairs

