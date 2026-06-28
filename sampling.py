import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

# =====================================
# Load Dataset from Local Path
# =====================================

#use full path
file_path = "C:/Users/deek/Downloads/data analytics/Day_8/Dataset.csv"
dataset = pd.read_csv(file_path)

# =====================================
# Dataset Information
# =====================================

print("\n===== Dataset Shape =====")
print(dataset.shape)

print("\n===== Statistical Summary =====")
print(dataset.describe())

print("\n===== First 5 Rows =====")
print(dataset.head())

# =====================================
# Simple Random Sampling
# =====================================

print("\n===== Simple Random Sampling =====")

simpleRandomSample = dataset.sample(n=5, random_state=42).sort_values(by="Id")

mean_simpleRandomSample = round(simpleRandomSample["SalePrice"].mean(), 3)

print("Mean of Simple Random Sample:", mean_simpleRandomSample)
print(simpleRandomSample)

# =====================================
# Systematic Sampling
# =====================================

print("\n===== Systematic Sampling =====")

index = np.arange(0, len(dataset), step=3)

systematicSample = dataset.iloc[index]

mean_systematicSample = round(systematicSample["SalePrice"].mean(), 3)

print("Mean of Systematic Sample:", mean_systematicSample)
print(systematicSample)

# =====================================
# Cluster Sampling
# =====================================

print("\n===== Cluster Sampling =====")

dataset_cluster = dataset.copy()

n = 5

dataset_cluster["cluster_id"] = np.repeat(
    range(1, n + 1),
    len(dataset_cluster) // n
)

index = []

for i in range(len(dataset_cluster)):
    if dataset_cluster["cluster_id"].iloc[i] % 2 == 0:
        index.append(i)

clusterSample = dataset_cluster.iloc[index]

mean_clusterSample = round(clusterSample["SalePrice"].mean(), 3)

print("Mean of Cluster Sample:", mean_clusterSample)
print(clusterSample)

# =====================================
# Stratified Sampling
# =====================================

print("\n===== Stratified Sampling =====")

dataset_strata = dataset.copy()

dataset_strata["strata"] = np.repeat(
    [1, 2],
    len(dataset_strata) // 2
)

split = StratifiedShuffleSplit(
    n_splits=1,
    test_size=8,
    random_state=42
)

for train_index, test_index in split.split(
        dataset_strata,
        dataset_strata["strata"]):

    stratifiedRandomSample = dataset_strata.iloc[test_index].sort_values(
        by="SalePrice"
    )

print(stratifiedRandomSample)