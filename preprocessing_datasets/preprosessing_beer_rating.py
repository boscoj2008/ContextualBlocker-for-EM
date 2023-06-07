#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper: Blocking Techniques for Entity Linkage: A Semantics-Based Approach

@author: Fabio Azzalini, Songle Jin, Marco Renzi, Letizia Tanca
"""
import pandas as pd
import os

def clean_beer_rate(): #CLEAN DATASETS

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname, '../source_datasets/Beer_rating/Beeradvo.csv')
    path_dataset2 = os.path.join(dirname, '../source_datasets/Beer_rating/Ratebeer.csv')
    path_dataset3 = os.path.join(dirname, '../source_datasets/Beer_rating/beeradvo_ratebeer_matches.csv')

    table1 = pd.read_csv(path_dataset1,encoding="ISO-8859-1")
    table2 = pd.read_csv(path_dataset2,encoding="ISO-8859-1")
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1")

   
    table3 = table1.append(table2, ignore_index=True)
    missing_values_replace = {
                           "Beer_Name": 'unk', 'Brew_Factory_Name': 'unk', 'Style': 'unk'
                              }

    table3.fillna(value=missing_values_replace, inplace=True)
    
    pairs = set()

    for pair in zip(table_match['ltable_id'], table_match['rtable_id']):
        ordered_pair = tuple(sorted((table3.loc[table3['id'] == pair[0]].index[0], table3.loc[table3['id'] == pair[1]].index[0])))
        pairs.add(ordered_pair)

    table3.drop('id', axis=1, inplace=True)
    attributes = table3.columns.values.tolist()[:-1]
    # info_task['range_set1'] = (0, len(table1.index))
    # info_task['range_set2'] = (len(table1.index), len(table3.index))
    for attr in attributes:
        table3[attr] = table3[attr].str.lower()

    return table3,pairs