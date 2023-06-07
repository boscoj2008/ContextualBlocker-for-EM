#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import os

def clean_google_GSM():

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname, '../source_datasets/Smart_phone_data/Amazon.csv')
    path_dataset2 = os.path.join(dirname, '../source_datasets/Smart_phone_data/GSMArena.csv')
    path_dataset3 = os.path.join(dirname, '../source_datasets/Smart_phone_data/perf_matches_amzn_gsm.csv')

    table1 = pd.read_csv(path_dataset1,encoding="ISO-8859-1")
    # dtype_Amazon = {'id': int, 'Brand': str, 'Type': str, 'Chipset': str, 'Screen_Dimension': str}
    table2 = pd.read_csv(path_dataset2,encoding="ISO-8859-1")
    # dtype_GSMArena = {'id':int, 'Brand': str, 'Type': str, 'Chipset': str, 'Screen_Dimension': str}
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1")

    table3 = table1.append(table2, ignore_index=True)
    #missing_values_replace = {"id": 'unk', "Brand": 'unk', 'Type': 'unk', 'Chipset': 'unk',
    #                          'Screen_Dimension': 'unk'}
  
    attributes = table3.columns.values.tolist()
    #table3.fillna(value=missing_values_replace, inplace=True)

    pairs = set()

    for pair in zip(table_match['ltable_id'], table_match['rtable_id']):
        ordered_pair = tuple(sorted((table3.loc[table3['ï»¿id'] == pair[0]].index[0], table3.loc[table3['ï»¿id'] == pair[1]].index[0])))
        pairs.add(ordered_pair)


    for attr in attributes[1:]:
        table3[attr] = table3[attr].str.lower()


    table3.drop('ï»¿id', axis=1, inplace=True)


    return table3,pairs

