# A Graph-Based Blocking Approach for Entity Matching Using Contrastively Learned Embeddings

abstract 

Data integration is considered a crucial task in the entity matching process. In this process, redundant and cunning entries must be identified and eliminated to improve the data quality. To archive this, a comparison between all entities is performed. However, this has quadratic computational complexity. To avoid this, `blocking' limits comparisons to probable matches. This paper presents a k-nearest neighbor graph-based blocking approach utilizing state-of-the-art context-aware sentence embeddings from pre-trained transformers. Our approach maps each database tuple to a node and generates a graph where nodes are connected by edges if they are related. We then invoke unsupervised community detection techniques over this graph and treat blocking as a graph clustering problem. Our work is motivated by the scarcity of training data for entity matching in real-world scenarios and the limited scalability of blocking schemes in the presence of proliferating data. Additionally, we investigate the impact of contrastively trained embeddings on the above system and test its capabilities on four data sets exhibiting more than 6 million comparisons. We show that our block processing times on the target benchmarks vary owing to the efficient data structure of the k-nearest neighbor graph. Our results also show that our method achieves better performance in terms of F1 score when compared to current deep learning-based blocking solutions.


Repository contains code for [A Graph-Based Blocking Approach for Entity Matching Using Contrastively Learned Embeddings](https://dl.acm.org/doi/abs/10.1145/3584014.3584017) published in ACM SIGAPP Applied Computing Review, Volume 22, Issue 4.

Requirements 
- python 3.9.7
- Transfomers library
- scikit-learn 1.1.2
- networkx 2.6.3
- community_louvain 0.16
- cdlib
- simcse library

To run;

```
 python contextual_blocker.py 
```


The meaning of flags:

- `--dataset: the dataset name e.g., walmart-amazon-clean`
- `--blocker: the blocking algorithm e.g., lovain or leiden`
- `--model_name: the model name to use in SimCSE e.g., RoBERTa or BERT`
- `--attributes: choose the attribute names to block on (performs better)`
- `--lower_limit: min number of neigbours to inspect in clusters e.g., 2`
- `--upper_limit: max number of neigbours to inspect in clusters e.g., 30`
- `--max_seq_length: token seq. length e.g., 200`
 

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

<img src="https://t.bkit.co/w_6433809da76a7.gif" />
