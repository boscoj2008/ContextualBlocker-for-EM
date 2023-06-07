#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
codes modified from: Blocking Techniques for Entity Linkage: A Semantics-Based Approach

"""

def load_dataset(key_values):
    
    if key_values['dataset'] == 'walmart-amazon-clean':
        from .preprocessing_amzn_wal import clean_amzn_walmart
        table, pairs = clean_amzn_walmart()
        
    elif key_values['dataset'] == 'walmart-amazon-dirty':
        from .preprocessing_amzn_wal import dirty_amzn_walmart
        table, pairs = dirty_amzn_walmart()
    
    elif key_values['dataset'] == 'itunes-amazon-clean':
        from .preprocessing_itunes_amazon import clean_amazon_itunes
        table, pairs = clean_amazon_itunes()
    
    elif key_values['dataset'] == 'itunes-amazon-dirty':
        from .preprocessing_itunes_amazon import dirty_amazon_itunes
        table, pairs = dirty_amazon_itunes()

    elif key_values['dataset'] == 'DBLP-Scholar-clean':
        from .preprocessing_dblp_scholar import clean_dblp_scholar
        table, pairs = clean_dblp_scholar()

    elif key_values['dataset'] == 'DBLP-Scholar-dirty':
        from .preprocessing_dblp_scholar_dirty import dirty_dblp_scholar
        table, pairs = dirty_dblp_scholar()

    elif key_values['dataset'] == 'company':
        from .preprocessing_company import company
        table, pairs = company()
        
        
    elif key_values['dataset'] == 'wdc_cameras':
        from .wdc_cameras import wdc_cameras
        table , pairs = wdc_cameras()

    if key_values['verbose'] > 0:
        print("#####################################################################")
        print("CURRENT dataset:        "+key_values['dataset'])
        print("CURRENT cluster_method: "+key_values['cluster_method'])
        print("CURRENT embedding_type: "+key_values['embedding_type'])
        print("#####################################################################")
    return key_values['dataset'], table, pairs

