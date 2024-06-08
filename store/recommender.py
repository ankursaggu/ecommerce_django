import numpy as np
from .cython_modules.recommend import recommend_products as cython_recommend_products

# Dummy data for product embeddings (use actual product features in a real scenario)
product_embeddings = np.random.rand(10, 5)  # 10 products with 5-dimensional embeddings

def recommend_products(product_id, top_n=5):
    return cython_recommend_products(product_id, product_embeddings, top_n)
