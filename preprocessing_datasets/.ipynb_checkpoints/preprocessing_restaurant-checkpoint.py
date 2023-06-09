#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper: Blocking Techniques for Entity Linkage: A Semantics-Based Approach

@author: Fabio Azzalini, Songle Jin, Marco Renzi, Letizia Tanca
"""
from .preprocessing_utilities import load_csv, lrstrip, setLowercase, setEmpty, createEntities, createPairs


def clean_restaurant():

    table = load_csv('../source_datasets/restaurant/restaurant.csv')
    attributes = table.columns.values.tolist()
    attributes = attributes[:-1]  # REMOVE last column

    table['class'] = table.loc[:, 'class'].str.replace("'", '')

    for attr in attributes:
        #table[attr] = table.loc[:, attr].str.replace('"', '')
        table[attr] = lrstrip(table, attr)
        setEmpty(table, attr)
        table[attr] = setLowercase(table, attr)

    entities = createEntities(table)
    table.drop('class', axis=1, inplace=True)
    return table, createPairs(entities)

# table, entities = clean_restaurant()

# print(table.iloc[0])
# print(entities)
