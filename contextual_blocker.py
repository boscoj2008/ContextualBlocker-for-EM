"""
A Graph-Based Blocking Approach for Entity Matching Using Contrastively Learned Embeddings 
Authors: John Bosco Mugeni & Toshiyuki Amagasa 
Institute: University of Tsukuba (ibaraki, Japan).

Published: ACM SIGAPP Applied Computing Review (Feb 2023)
"""


import argparse
import time
from preprocessing_datasets import load_dataset
from evaluation import calc_index
from graph_clustering.knn_graph_clusteriser import all_in_one_clusteriser
#from vector_models import model
from transformers import AutoTokenizer
from simcse import SimCSE



parser = argparse.ArgumentParser(description='Graph-based Block Clustering')

parser.add_argument("--verbose", type=int, default='0',choices=[0, 1, 2], help="increase output verbosity")
parser.add_argument("--dataset", type=str,default='walmart-amazon-clean', help='dataset')
parser.add_argument("--blocker", type=str,default='louvain', help='clustering algorithm')
parser.add_argument("--num_clusters", type=int,default='6', help='used in knn graph')
parser.add_argument("--attributes", default=["title", "brand"], nargs='+')
parser.add_argument("--model_name", type=str, default='princeton-nlp/sup-simcse-bert-base-uncased',help="model_path or name")
parser.add_argument("--upper_limit", type=int, default='30', help='upper limit for n_neighbors' )
parser.add_argument("--lower_limit", type=int, default='2', help='lower limit for n_neighbors' )
parser.add_argument("--step", type=int, default='1', help='step size' )
parser.add_argument("--max_seq_length", type=int, default=256, help='models sequence length')

hp, _ = parser.parse_known_args()

key_values = {
    'dataset': hp.dataset,
    'cluster_method': hp.blocker,
    'verbose': hp.verbose,
    'num_clusters': hp.num_clusters,
    'attributes_list': hp.attributes,
    'model_name': hp.model_name,
}

######################################
########### Blocking program ##########
######################################

prog_start = time.time()
# 1) LOAD and PREPROCESS the dataset

dataset_name, table, pairs = load_dataset(key_values)

# 2) DO the embedding

start = time.time()
attributes = hp.attributes # get attr names
records = table[attributes].agg(' '.join, axis=1)
#transformer = model(hp) # uncomment if needed
simCSE = SimCSE(hp.model_name) # pre-trained model 

print(f'constucting embedding space chosen attributes: {attributes}')
vectors = simCSE.encode(list(records), device="cuda", max_length=hp.max_seq_length)
print("TIME: {:.2f}".format(time.time() - start))



time_list = list()
key_values = {}

for num_clusters in range(hp.lower_limit, hp.upper_limit+1, hp.step):
    print()
    
    key_values["num_clusters"] = num_clusters
    print(f"building blocks with: {num_clusters} clusters")
    
    start = time.time()
    data = all_in_one_clusteriser(vectors, hp.blocker, num_clusters)
    reduction_ratio, pair_completeness, reference_metric, pair_quality, fmeasure = calc_index(data, table, pairs)
    
    
    print("(RR) Reduction ratio is: {:.2f}".format(reduction_ratio))
    print("(PC) Pair completeness is: {:.2f}".format(pair_completeness))
    print("(RM) Reference metric (Harmonic mean RR and PC) is: {:.2f}".format(reference_metric))
    
    end = time.time()
    blocking_time = end - start
    time_list.append(blocking_time)  # blocking time for 30 loops
    
    print(">> Blocking time was roughly {:.2f} seconds for {} tuples!".format(blocking_time, vectors.shape[0]))
    print("*" * 50)



