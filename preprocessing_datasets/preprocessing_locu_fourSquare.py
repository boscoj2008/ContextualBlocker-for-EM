#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper: 

@author: John Bosco
"""

import pandas as pd
import os

def clean_locu_fourSquare():

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname, '../source_datasets/Entity-Resolution/locu_train.json')
    path_dataset2 = os.path.join(dirname, '../source_datasets/Entity-Resolution/foursquare_train.json')
    path_dataset3 = os.path.join(dirname, '../source_datasets/Entity-Resolution/matches_train.csv')

    table1 = pd.read_json(path_dataset1)
    
    table2 = pd.read_json(path_dataset2)
    # dtype_match = {'idDBLP': str, "idACM": str}
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1")

    table3 = table1.append(table2, ignore_index=True)
    missing_values_replace = {"latitude": 'unk', "logitude": 'unk', "phone": 'unk'}
    table3 = table3[['id','country', 'latitude', 'locality', 'longitude', 'name', 'phone', 'postal_code', 'region', 'street_address', 'website']]
    attributes = table3.columns.values.tolist()
    table3.longitude = table3.longitude.astype('str')
    table3.latitude = table3.latitude.astype('str')
    table3.fillna(value=missing_values_replace, inplace=True)

    pairs = set()

    for pair in zip(table_match['locu_id'], table_match['foursquare_id']):
        ordered_pair = tuple(sorted((table3.loc[table3['id'] == pair[0]].index[0], table3.loc[table3['id'] == pair[1]].index[0])))
        pairs.add(ordered_pair)


    for attr in attributes[1:]:
        table3[attr] = table3[attr].str.lower()


    table3.drop('id', axis=1, inplace=True)


    return table3,pairs


