import numpy as np
cimport numpy as np

def recommend_products(int product_id, np.ndarray[np.float64_t, ndim=2] product_embeddings, int top_n=5):
    cdef int i
    cdef int num_products = product_embeddings.shape[0]
    cdef np.ndarray[np.float64_t, ndim=1] similarities = np.zeros(num_products, dtype=np.float64)
    cdef np.ndarray[np.float64_t, ndim=1] product_vector = product_embeddings[product_id]

    for i in range(num_products):
        similarities[i] = np.dot(product_embeddings[i], product_vector)

    cdef np.ndarray[np.int32_t, ndim=1] similar_indices = np.argsort(similarities)[::-1][1:top_n+1]
    return similar_indices.tolist()
