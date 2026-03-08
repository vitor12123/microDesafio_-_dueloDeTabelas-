import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('dataset_ecommerce.csv')

melhoresAvaliacoes = df.sort_values('review_score', ascending=False).head(2)
melhoresAvaliacoes[ ['product_name', 'review_score'] ]