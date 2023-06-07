from sentence_transformers import SentenceTransformer, models
from torch import nn
from transformers import AutoModel, AutoTokenizer


def model(hp):
    word_embedding_model = models.Transformer(hp.model_name, hp.max_seq_length)
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                                   pooling_mode_mean_tokens=True, pooling_mode_max_tokens=False)
    transformer = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    return transformer


def smcse(hp, inputs):
    model = AutoModel.from_pretrained(hp.model_name)

    # Get the embeddings
    with torch.no_grad():
        embeddings = model(**inputs, output_hidden_states=True, return_dict=True).pooler_output
    return embeddings

