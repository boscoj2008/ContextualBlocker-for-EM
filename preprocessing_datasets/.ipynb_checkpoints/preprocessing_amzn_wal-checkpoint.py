#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os
import re
import numpy as np


def clean_amzn_walmart(): #CLEAN DATASETS

    dirname = os.path.dirname(__file__)
    path_dataset1 = os.path.join(dirname,  '../source_datasets/Walmart-Amazon/tableA.csv')
    path_dataset2 = os.path.join(dirname,  '../source_datasets/Walmart-Amazon/tableB.csv')
    path_dataset3 = os.path.join(dirname,  '../source_datasets/Walmart-Amazon/matches.csv')

    table1 = pd.read_csv(path_dataset1,encoding="ISO-8859-1") # wal
    table2 = pd.read_csv(path_dataset2,encoding="ISO-8859-1") # amz
    table_match = pd.read_csv(path_dataset3,encoding="ISO-8859-1", ) # perfect matches
    
    # convert price 
    table1['price'] = table1['price'].astype('str')
    table2['price'] = table2['price'].astype('str')
    #table2['shipweight'] = table2['shipweight'].astype('str')
    
    # extact values from shipweight in table 1
    #def split_it(str):
        #return re.findall('\d*\.?\d+', str)[0]
    
    # handle na's
    #missing_val_df =  table1[table1.isna().shipweight]
    # table1.shipweight = table1.shipweight.replace("nan", np.nan)
#     table1.price = table1.price.replace("nan", np.nan)

#     table2.price = table2.price.replace("nan", np.nan)
#     missing_val_df.price = missing_val_df.price.replace("nan", np.nan)
#     missing_val_df.shipweight = missing_val_df.shipweight.replace("nan", np.nan)
    table3 = table1.append(table2, ignore_index=True) # append table
    
#     table3 = table3.append(missing_val_df, ignore_index=True)
    missing_values_replace = {"category": 'unk', "brand": 'unk', "model": 'unk',
                              'price': '0', 'modelno':"unk"} # missing value tokens
    
    
    attributes = table3.columns.values.tolist()
    
    table3.fillna(value=missing_values_replace, inplace=True)

    
    

    pairs = set()

    for pair in zip(table_match['ltable_id'], table_match['rtable_id']):
        ordered_pair = tuple(sorted((table3.loc[table3['id'] == pair[0]].index[0], table3.loc[table3['id'] == pair[1]].index[0])))
        pairs.add(ordered_pair)
        
    for attr in attributes[1:]:
        table3[attr] = table3[attr].str.lower()

    table3.drop(labels=['id'], axis=1, inplace=True)
    # info_task['range_set1'] = (0, len(table1.index))
    # info_task['range_set2'] = (len(table1.index), len(table3.index))

    return table3,pairs