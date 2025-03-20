import kagglehub

# Download latest version
path = kagglehub.dataset_download("tunguz/big-five-personality-test")

print("Path to dataset files:", path)

import os

# 'path' is the folder path printed by your initial code
print("Files in dataset directory:", os.listdir(path))

import pandas as pd

data_file = os.path.join(path, 'data-final.csv')
df = pd.read_csv(data_file)
